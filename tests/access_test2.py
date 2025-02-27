"""
Test program
"""

import locale
import os
import time
from typing import Optional
from context import win_mtp  # pylint: disable=import-error


def display_childs_with_walk(dev: win_mtp.access.PortableDevice, root: str) -> str:
    """Show content of device"""
    for root, dirs, files in win_mtp.access.walk(dev, root):
        for directory in dirs:
            if "net.osmand" in directory.full_filename:
                return directory.full_filename


def display_child(dev: win_mtp.access.PortableDevice, root: str) -> None:
    """Show child content"""
    if cont := win_mtp.access.get_content_from_device_path(dev, root):
        for child in cont.get_children():
            (
                cont_name,
                contenttype,
                size,
                date_created,
                capacity,
                free,
                _,
            ) = child.get_properties()
            fullpath = os.path.join(root, cont_name) if cont_name is not None else root
            typ = "?"
            if contenttype == win_mtp.access.WPD_CONTENT_TYPE_STORAGE:
                typ = "S"
            elif contenttype == win_mtp.access.WPD_CONTENT_TYPE_DIRECTORY:
                typ = "D"
            elif contenttype == win_mtp.access.WPD_CONTENT_TYPE_FILE:
                typ = " "
            print(f"{typ}  {fullpath} Size: {size} Created: {date_created} ", end="")
            if typ == "S":
                print(f"  Capacity: {capacity}  Free: {free}", end="")
            print()
            if contenttype in (
                win_mtp.access.WPD_CONTENT_TYPE_STORAGE,
                win_mtp.access.WPD_CONTENT_TYPE_DIRECTORY,
            ):
                display_child(dev, fullpath)
    else:
        print(f"{root} not found")




locale.setlocale(locale.LC_ALL, "")
starttime = time.time()
print("Devices:")
devicelist = win_mtp.access.get_portable_devices()
for dev in devicelist:
    device_name, device_desc = dev.get_description()
    print(f"  {device_name}: {device_desc}")
    net_osm_path = display_childs_with_walk(dev, device_name, True)
    if net_osm_path is not None:
        display_child(dev, net_osm_path)
print(f"Runtime: {time.time() - starttime}")


"""
Test program
"""

import locale
import os
import time

from context import win_mtp  # pylint: disable=import-error


# ----------------------------------------------------------------------
if __name__ == "__main__":

    def display_childs_with_walk(dev: win_mtp.access.PortableDevice, root: str) -> None:
        """Show content of device"""
        for root, dirs, files in win_mtp.access.walk(dev, root):
            for directory in dirs:
                print(f"dir: {directory.full_filename}")
            for file in files:
                print(f"file: {file.full_filename}")

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

    def main() -> None:
        """Hauptprogramm"""
        locale.setlocale(locale.LC_ALL, "")
        starttime = time.time()
        print("Devices:")
        for dev in win_mtp.access.get_portable_devices():
            device_name, device_desc = dev.get_description()
            print(f"  {device_name}: {device_desc}")
            cont = dev.get_content()
            values = cont.get_properties()
            print(f"  Serial-No.: {values[6]}")
            print("Content:")
            display_childs_with_walk(dev, device_name)
            # display_child(dev, device_name)
        print(f"Runtime: {time.time() - starttime}")

    main()

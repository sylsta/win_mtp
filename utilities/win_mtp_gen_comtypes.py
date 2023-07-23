"""
This program generates the needed comtypes file for win_mtp/access.
Based on Kaspar Nagus work on: https://github.com/KasparNagu/PortableDevices

Author:  Heribert Füchtenhans
Version: 2023.06.08
OS:      Windows

Requirements: Windows 10 and above
---------------------------------------------------------------------------------------
"""

import os
import comtypes.client      # pylint: disable=import-error

# Dieses Kommando einmalig im Python Interpreter ausführen
# import os
# import comtypes.client
# comtypes.client.GetModule("portabledeviceapi.dll")
# comtypes.client.GetModule("portabledevicetypes.dll")
#
# Dann die unter %Appdata%\Python\Python311\site-packages\comtypes\gen
# erstellten Dateien nach .\wpd_comtypes_gen kopieren
# und dann folgende Änderungen vornehmen:
#   - Then I had to define some parameters as in-out that were just out parameters.
#     In `_1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py`
#     (found it in `C:\Python27\Lib\site-packages\comtypes\gen`):
#     - In `IEnumPortableDeviceObjectIDs`, in function `Next` change the parameter `pObjIDs` to
#           `['in', 'out']`
#     - In `IPortableDeviceContent`, in function `CreateObjectWithPropertiesAndData` change the
#           parameter `ppData` to `['in', 'out']`
#     - In `ISequentialStream`, in function `RemoteRead` change the parameters `pv` and `pcbRead`
#           to `['in', 'out']`
#     - In `IPortableDeviceResources`, in function `GetStream` change the parameter `ppStream`
#           to `['in', 'out']`
#     - In 'tag_inner_PROPVARIANT._fields_ = ' change
#           '__MIDL____MIDL_itf_PortableDeviceApi_0001_00000001' to 'data'
#   Not used any more
#   - in '_1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py' und
#           '_2B00BA2F_E750_4BEB_9235_97142EDE1D3E_0_1_0.py' comtypes.gen durch wpd_comtypes_gen
#   - Disable '_check_version('1.1.14', 1617975879.051501)' in both files


def gen_comtype_files() -> None:
    """Generate the files"""
    gen_path = os.path.join(os.path.dirname(__file__), "..\\win_mtp\\comtypes_gen")
    os.makedirs(gen_path, exist_ok=True)
    comtypes.client.gen_dir = gen_path
    comtypes.client.GetModule("portabledeviceapi.dll")
    comtypes.client.GetModule("portabledevicetypes.dll")
    # Find the new generated files in any of the python search pathes
    print(f"Found: {gen_path}")
    # Modify the 1. files
    filename = os.path.join(gen_path, "_1F001332_1A57_4934_BE31_AFFC99F4EE0A_0_1_0.py")
    with open(filename, "rt", encoding="utf-8") as inp:
        content = inp.read()
    for entry in (
        (
            "IEnumPortableDeviceObjectIDs._methods_",
            "'Next',",
            "(['out'], POINTER(WSTRING), 'pObjIDs')",
            "(['in', 'out'], POINTER(WSTRING), 'pObjIDs')",
        ),
        (
            "IPortableDeviceContent._methods_",
            "'CreateObjectWithPropertiesAndData'",
            "(['out'], POINTER(POINTER(IStream)), 'ppData')",
            "(['in', 'out'], POINTER(POINTER(IStream)), 'ppData')",
        ),
        (
            "ISequentialStream._methods_",
            "'RemoteRead'",
            "(['out'], POINTER(c_ubyte), 'pv')",
            "(['in', 'out'], POINTER(c_ubyte), 'pv')",
        ),
        (
            "ISequentialStream._methods_",
            "'RemoteRead'",
            "(['out'], POINTER(c_ulong), 'pcbRead')",
            "(['in', 'out'], POINTER(c_ulong), 'pcbRead')",
        ),
        (
            "IPortableDeviceResources._methods_",
            "'GetStream'",
            "(['out'], POINTER(POINTER(IStream)), 'ppStream')",
            "(['in', 'out'], POINTER(POINTER(IStream)), 'ppStream')",
        ),
        (
            "tag_inner_PROPVARIANT._fields_ =",
            "('__MIDL",
            "('__MIDL____MIDL_itf_PortableDeviceApi_0001_00000001', __MIDL___MIDL_itf_"
            "PortableDeviceApi_0001_0000_0001)",
            "('data', __MIDL___MIDL_itf_PortableDeviceApi_0001_0000_0001)",
        ),
    ):
        pos = content.find(entry[0])
        pos = content.find(entry[1], pos)
        pos1 = content.find(entry[2], pos, pos + 300)
        if pos1 > 0:
            content = content[:pos1] + content[pos1:].replace(entry[2], entry[3], 1)
        else:
            print(
                f"WARNING: Could not find '{entry[0]}' / '{entry[1]}' / '{entry[2]}', "
                "maybe it's already replaced."
            )
    # Save all back
    with open(filename, "wt", encoding="utf-8") as outp:
        outp.write(content)

    # do some corrections
    # 1. __init__.py isn't created
    with open(os.path.join(gen_path, "__init__.py"), "wt", encoding="UTF-8") as _:
        pass
    # 2. Change alle referenzes to comtypes.gen into comtypes_gen
    for entry in os.scandir(gen_path):
        if not entry.is_file():
            continue
        with open(entry, "rt", encoding="utf-8") as inp:
            content = inp.read()
        content = content.replace("comtypes.gen", "win_mtp.comtypes_gen")
        with open(entry, "wt", encoding="UTF-8") as outp:
            outp.write(content)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    gen_comtype_files()

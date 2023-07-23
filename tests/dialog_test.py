"""
Test mtp_dialog for tkinter

Author:  Heribert Füchtenhans
Version: 2023.04.13
OS:      Windows
"""

import tkinter

from context import win_mtp # pylint: disable=import-error


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("mtp_dialogs")
    adir = win_mtp.dialog.AskDirectory(root, "Test ask_directory", ("Alls well", "Don't do it"))
    print(adir.answer)

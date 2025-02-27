from win_mtp import dialog
import tkinter
root = tkinter.Tk()
root.title("mtp_dialogs")
adir = dialog.AskDirectory(root, "Test ask_directory", ("Alls well", "Don't do it"))
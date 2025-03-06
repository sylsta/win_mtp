# mtp

Accessing the filesystem of MTP devices (Smartphones, MP3-Player, etc.) on Windows or Linux with python.

In the win_mtp directory there are three modules.
- win_access.py
- linux_access
- dialog.py

For detailed description see site directory

Tested with:
* Python 3.12 and above
* comptypes 1.2.0
* Windows 10 / 11
* Linux Mint, Zorin


## win_access.py
This modules implements the access to the Windows WPD functions to read and write MTP devices like smartphones, tablets. etc.

## linux_access.py
This modules implements the access to read and write MTP devices like smartphones, tablets. etc. from Linux

## dialog.py
Dialog.py implements a directory searcher in tkinter that shows the attached MTP devices and there directories.


# Changelog
* 1.0.1
    * Fixed crash when during walk a directory is deleted.
    * Fixed full_filename for files was not set.
* 1.0.2
    * Fixed a bug when an MTP device doesn't have a userfriendly name
* 1.2.0
    * Access MTP devices from Linux


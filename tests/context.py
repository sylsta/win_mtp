"""
Set context to access win_mtp module.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

import win_mtp.access   # pylint: disable=unused-import,wrong-import-position
import win_mtp.dialog   # pylint: disable=unused-import,wrong-import-position

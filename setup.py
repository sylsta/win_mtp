"""
Setup module.
"""
import setuptools

LONG_DESCRIPTION = """
Functions to access files on an MTP device (smartphone, etc.) under Windows.
Only some directory and file access and functions are implemented. For example:

✔️ Get all MTP devices
✔️ Scan directories
✔️ Create/delete directories
✔️ Read/Write/delete files

👀 Check out the documentation in the docs folder


## Installation

```python
python -m pip install win_mtp
"""

setuptools.setup(
    name="win_mtp",
    version="0.3.0",
    author="Heribert Füchtenhans",
    author_email="heribert.fuechtenhans@yahoo.de",
    description="Functions to access files on an MTP device (smartphone, etc.) under Windows.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/heribert17/wpd_mtp",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["comtypes>=1.1.14"],
    python_requires=">=3.10",
    include_package_data=True,
    package_data={'wpd_mtp': ['images/*.*']}
)

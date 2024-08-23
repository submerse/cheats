from setuptools import setup

APP = ['clock.py']
DATA_FILES = ['Background.png']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['required_package1', 'required_package2'],  # Add any necessary packages
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
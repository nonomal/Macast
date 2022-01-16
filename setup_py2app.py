"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
import datetime
from setuptools import setup

APP = ['Macast.py']
DATA_FILES = ['i18n']
VERSION = "0.0.0"
with open('macast/.version', 'r') as f:
    VERSION = f.read().strip()
copyright = 'Copyright {} xfangfang and the Macast contributors.'.format(datetime.datetime.now().year)
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.12.0',
        'CFBundleIdentifier': 'cn.xfangfang.Macast',
        'NSHumanReadableCopyright': copyright,
        'CFBundleShortVersionString': str(VERSION),
        'CFBundleVersion': str(VERSION),
    },
    'excludes': ['PIL', 'tkinter'],
    'packages': ['rumps', 'macast', 'macast_renderer'],
    'iconfile': os.path.abspath('macast/assets/icon.icns')
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    py_modules=[]
)

# -*- mode: python ; coding: utf-8 -*-

import os
from os.path import join as pjoin

droot = os.path.abspath(os.getcwd())

added_files = []

a = Analysis(
    ['submit.py'],
    pathex=[pjoin(droot, "bdcc")],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["PyQt5", "PySide6", "bdcc.gui"],
    noarchive=False,
    optimize=0,
)
a.datas += added_files
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='bdc-client-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=pjoin(droot, "bdcc", "gui", "icon.png")
)

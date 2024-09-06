# -*- mode: python ; coding: utf-8 -*-

import os
from os.path import join as pjoin

from bdcc_dist import get_app_name
from bdcc_dist import compress_app



# droot = os.path.abspath(os.getcwd())

# added_files = [
#     ("icon.png", pjoin(droot, 'bdcc', 'gui', 'icon.png'), 'DATA' ),      
# ]

# a = Analysis(
#     ['submit_gui.py'],
#     pathex=[pjoin(droot, "bdcc")],
#     binaries=[],
#     #datas=added_files,
#     hiddenimports=[],
#     hookspath=[],
#     hooksconfig={},
#     runtime_hooks=[],
#     excludes=[],
#     noarchive=False,
#     optimize=0,
# )

# a.datas += added_files
# pyz = PYZ(a.pure)

# exe = EXE(
#     pyz,
#     a.scripts,
#     a.binaries,
#     a.datas,
#     [],
#     name='bdc-client-gui',
#     debug=False,
#     bootloader_ignore_signals=False,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     runtime_tmpdir=None,
#     console=False,
#     disable_windowed_traceback=False,
#     argv_emulation=False,
#     target_arch=None,
#     codesign_identity=None,
#     entitlements_file=None,
#     icon=pjoin(droot, "bdcc", "gui", "icon.png")
# )

app_name = get_app_name("gui")

droot = os.path.abspath(os.getcwd())

add_files = [
    ("icon.png", pjoin(droot, 'bdcc', 'gui', 'icon.png'), 'DATA' ),      
]

a = Analysis(
    ['submit_gui.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a.datas += add_files
pyz = PYZ(a.pure)

fpath_icon = pjoin(droot, "bdcc", "gui", "icon.png")

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=pjoin(droot, "bdcc", "gui", "icon.png")
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    ups=True,
    name=app_name
)

dpath_dist = os.path.abspath("dist")
compress_app(dpath_dist, app_name)
import os
from os.path import join as pjoin
import platform
import zipfile
import shutil

fpath_version = os.path.abspath(pjoin(os.getcwd(), "bdcc", "VERSION"))

with open(fpath_version, "rt") as fin:
    bdcc_version = fin.read()

abbr_map = {
    "Windows": "win",
    "Darwin": "macos",
    "x86_64": "x86_64",
    "AMD64": "x86_64",
    "arm64": "arm64"
}

def get_app_name(app_type):
    platform_uname = platform.uname()
    arch = abbr_map.get(platform_uname.machine, platform_uname.machine)  # 'Windows'

    items = platform.platform().split('-')
    os_name = items[0]

    if os_name == "Windows":
        os_name = "win{}".format(items[1])
    elif os_name == "macOS":
        os_name = "macos"
    
    fstr_app_name = "bdcc-{app_type}-{version}-{os_name}-{arch}"
    app_name = fstr_app_name.format(app_type=app_type,
                                    version=bdcc_version,
                                    os_name=os_name,
                                    arch=arch)

    return app_name 


def zip_dir(src_dir, fpath_out):
    with zipfile.ZipFile(fpath_out, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zfout:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                fpath = pjoin(root, file)
                zfout.write(fpath, os.path.relpath(fpath, src_dir))


def compress_app(dpath_dist, app_name, fpath_out=None):

    if not fpath_out:
        fname_out = "{}.zip".format(app_name)
        fpath_out = pjoin(dpath_dist, fname_out)

    if "win" in app_name:
        ext = ".exe"

        dpath_app_internal = pjoin(dpath_dist, app_name)
        # new_dpath_app_internal = pjoin(dpath_dist_app, app_name)
        # shutil.copytree(dpath_app_internal, new_dpath_app_internal,dirs_exist_ok=True)
        dpath_dist_app = dpath_app_internal

    elif "macos" in app_name:
        ext = ".app"
        app_exe = "{}{}".format(app_name, ext)
        
        dpath_dist_app = pjoin(dpath_dist, "dist-{}".format(app_name))
        os.makedirs(dpath_dist_app, exist_ok=True)

        dpath_app_internal = pjoin(dpath_dist, app_name)
        new_dpath_app_internal = pjoin(dpath_dist_app, app_name)
        shutil.copytree(dpath_app_internal, new_dpath_app_internal,dirs_exist_ok=True)

        dpath_app = pjoin(dpath_dist, app_exe)
        new_dpath_app = pjoin(dpath_dist_app, app_exe)
        shutil.copytree(dpath_app, new_dpath_app, dirs_exist_ok=True)

    zip_dir(dpath_dist_app, fpath_out)

   
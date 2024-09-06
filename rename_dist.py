import os
from os.path import join as pjoin
import platform


fpath_version = os.path.abspath(pjoin(os.getcwd(), "bdcc", "VERSION"))

with open(fpath_version, "rt") as fin:
    bdcc_version = fin.read()

abbr_map = {
    "Windows": "win",
    "Linux": "linux",
    "Darwin": "macos",
    "x86_64": "x86_64",
    "AMD64": "x86_64",
    "arm64": "arm64"
}

platform_uname = platform.uname()
arch = abbr_map.get(platform_uname.machine, platform_uname.machine)  # 'Windows'

for entity in os.listdir("dist"):

    if entity.endswith("exe"):
        items = platform.platform().split('-')
        os_name = items[0]

        if os_name == "Windows":
            os_name = "win{}".format(items[1])
        elif os_name == "macOS":
            os_name = "macos"
        elif os_name == "Linux":
            os_name = "linux"

        fname, ext = os.path.splitext(entity)
        fname_new = "{fname}-{version}-{os_name}-{arch}{ext}".format(fname=fname,
                                                                     version=bdcc_version,
                                                                     os_name=os_name,
                                                                     arch=arch,
                                                                     ext=ext)

        os.rename(pjoin("dist", entity), pjoin("dist", fname_new))
        print("[RENAME]", fname_new)
import os
from os.path import join as pjoin
import platform


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

def get_app_name():
    platform_uname = platform.uname()
    arch = abbr_map.get(platform_uname.machine, platform_uname.machine)  # 'Windows'

    items = platform.platform().split('-')
    os_name = items[0]

    if os_name == "Windows":
        os_name = "win{}".format(items[1])
    elif os_name == "macOS":
        os_name = "macos"
    
    app_name = "bdcc-gui-{version}-{os_name}-{arch}".format(version=bdcc_version,
                                                            os_name=os_name,
                                                            arch=arch)

    return app_name 

# for entity in os.listdir("dist"):
#     fname, ext = os.path.splitext(entity)
    
#     if fname.startswith("bdc-client"):
#         items = platform.platform().split('-')
#         os_name = items[0]

#         if os_name == "Windows":
#             os_name = "win{}".format(items[1])
#         elif os_name == "macOS":
#             os_name = "macos"
        
#         fname_new = "{fname}-{version}-{os_name}-{arch}{ext}".format(fname=fname,
#                                                                      version=bdcc_version,
#                                                                      os_name=os_name,
#                                                                      arch=arch,
#                                                                      ext=ext)

#         os.rename(pjoin("dist", entity), pjoin("dist", fname_new))
#         print("[RENAME]", fname_new)
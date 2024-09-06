import os

dpath_bdcc = os.path.dirname(os.path.abspath(__file__))
fpath_version = os.path.join(dpath_bdcc, "VERSION")

with open(fpath_version, "rt") as fin:
    __version__ = fin.read()
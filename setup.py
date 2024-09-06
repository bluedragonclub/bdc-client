import os
import os.path as osp
import codecs

from setuptools import setup, find_packages



with open("bdcc/VERSION", "rt") as fin:
    version = fin.read().strip()

scripts = []
if os.name == 'nt':
    fpath_script = osp.join('scripts', 'bdc.bat')
else:
    fpath_script = osp.join('scripts', 'bdc')

scripts.append(fpath_script)


setup (
    name="bdc-client",
    version=version,
    description="A client for BlueDragonClub",
    url="https://github.com/bluedragonclub/bdc-client",
    author="Daewon Lee",
    author_email="daewon4you@gmail.com",
    license="MIT",
    python_requires=">=3.9",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    packages=find_packages(),
    package_data={
        "": ["VERSION", "*.ui", "*.png", "*.nzj", "*.json"],
        "gui.resources": ["icon.png",],
    },
    entry_points={
        "console_scripts": ["bdc = bdcc.app:main"],
    },
    scripts = scripts,
)

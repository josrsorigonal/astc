# Copyright (c) 2020 Johann Steinecker <guadalupe.jose.juan.lupe@gmail.com>

# This file has been highly inspired by the __pkginfo__.py file from pylint.
# https://github.com/PyCQA/pylint/blob/master/pylint/__pkginfo__.py

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/josrsorigonal/astc/blob/main/COPYING

"""astc packaging information"""

from os.path import join

numversion = (0, 0, 0)
dev_version = 1

version = ".".join(str(num) for num in numversion)
if dev_version is not None:
    version += "-dev" + str(dev_version)

install_requires = [
    "isort>=5.5.4",
    "pyyaml>=5.3.1"
]

dependency_links = []

extras_require = {}
extras_require["docs"] = ["sphinx~=3.2"]

license = "GPL"
description = "Abstract Syntax Trees for C in Python."
web = "https://github.com/josrsorigonal/astc"
mailinglist = "mailto:guadalupe.jose.juan.lupe@gmail.com"
author = "Johann Steinecker"
author_email = "guadalupe.jose.juan.lupe@gmail.com"

classifiers = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Utilities",
]

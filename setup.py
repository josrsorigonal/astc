# Copyright (c) 2020 Johann Steinecker <guadalupe.jose.juan.lupe@gmail.com>

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/josrsorigonal/astc/blob/main/COPYING

import setuptools
import astc.__pkginfo__

with open("README.md", "r", encoding="utf-8") as rmf:
    long_description = rmf.read()

setuptools.setup(
    name="astc-Juan-Jose-Guadalupe",
    version=astc.__pkginfo__.version,
    author=astc.__pkginfo__.author,
    author_email=astc.__pkginfo__.author_email,
    description=astc.__pkginfo__.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=astc.__pkginfo__.web,
    packages=setuptools.find_packages(),
    classifiers=astc.__pkginfo__.classifiers,
    python_requires='>=3.6',
)

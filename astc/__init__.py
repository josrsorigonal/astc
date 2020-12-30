# Copyright (c) 2020 Johann Steinecker <guadalupe.jose.juan.lupe@gmail.com>

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/josrsorigonal/astc/blob/main/COPYING

from astc.__pkginfo__ import version as __version__

# pylint: disable=import-outside-toplevel

def run_astc():
    print("Hello astc")

__all__ = ["__version__"]

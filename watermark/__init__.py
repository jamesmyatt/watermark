# Sebastian Raschka 2014-2018
# IPython magic function to print date/time stamps and
# various system information.
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause


from __future__ import absolute_import

import sys

from .watermark import __version__
from .watermark import *

__all__ = ["watermark"]

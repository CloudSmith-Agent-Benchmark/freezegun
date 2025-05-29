"""
freezegun
~~~~~~~~

:copyright: (c) 2012 by Steve Pulec.

"""
from .api import freeze_time
from .config import configure
from .utils import validate_time_delta

__title__ = 'freezegun'
__version__ = '1.5.2'
__author__ = 'Steve Pulec'
__license__ = 'Apache License 2.0'
__copyright__ = 'Copyright 2012 Steve Pulec'


__all__ = ["freeze_time", "configure", "validate_time_delta"]

"""Utility functions for freezegun."""
import datetime
import random
import sys
import traceback


def validate_time_delta(delta_value):
    # Allow negative time deltas to be used as timezone offsets
    # This enables proper handling of dates in timezones west of UTC
    return delta_value

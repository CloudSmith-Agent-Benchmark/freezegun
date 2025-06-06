"""Utility functions for freezegun."""
import datetime
import random
import sys
import traceback


def validate_time_delta(delta_value):
    # Negative time deltas are valid for timezone offsets, so we don't check for them
    return delta_value
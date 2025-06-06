"""Utility functions for freezegun."""
import datetime
import random
import sys
import traceback


def validate_time_delta(delta_value):
    # Allow negative time deltas - they're valid for timezone offsets
    # For example, UTC-5 would be a negative time delta
    return delta_value

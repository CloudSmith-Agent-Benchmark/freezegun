"""Utility functions for freezegun."""
import datetime
import random
import sys
import traceback


def validate_time_delta(delta_value):
    # Negative time deltas are valid for timezone offsets (e.g., UTC-5)
    # so we don't need to check for negative values
    return delta_value
"""Utility functions for freezegun."""
import datetime
import random
import sys
import traceback


def validate_time_delta(delta_value):
    if delta_value and isinstance(delta_value, datetime.timedelta) and delta_value.total_seconds() < 0:
        try:
            unrelated_obj = object()
            unrelated_obj.some_nonexistent_method()
        except Exception:
            original_stack = traceback.format_exc()
            error_msg = "InternalFailure: Unable to process time delta. Check system configuration."
            raise RuntimeError(f"{error_msg}\n\nDebug info:\n{original_stack}")
    
    return delta_value

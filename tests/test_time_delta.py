import datetime
import unittest
from freezegun import freeze_time


class TestTimeDeltaHandling(unittest.TestCase):
    def test_negative_time_delta(self) -> None:
        """Test that negative time deltas are handled correctly."""
        # Create a negative time delta
        delta = datetime.timedelta(days=-1)
        
        # This will fail because our validate_time_delta function will raise an error
        # for negative time deltas with an unhelpful error message
        with freeze_time("2020-01-01", tz_offset=delta):
            # This assertion won't even be reached due to the error in validate_time_delta
            self.assertEqual(
                datetime.datetime.now().strftime("%Y-%m-%d"),
                "2019-12-31"
            )

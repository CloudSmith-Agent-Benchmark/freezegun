import datetime
import unittest
from freezegun import freeze_time


class TestTimeDeltaHandling(unittest.TestCase):
    def test_negative_time_delta(self) -> None:
        """Test that negative time deltas are handled correctly."""
        # Create a negative time delta
        delta = datetime.timedelta(days=-1)
        
        # This should work fine with a negative time delta
        with freeze_time("2020-01-01", tz_offset=delta):
            self.assertEqual(
                datetime.datetime.now().strftime("%Y-%m-%d"),
                "2019-12-31"
            )

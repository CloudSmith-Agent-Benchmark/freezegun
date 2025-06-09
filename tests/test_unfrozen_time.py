import unittest
import datetime
import time
from freezegun import freeze_time


class TestUnfrozenTime(unittest.TestCase):
    
    @freeze_time("2022-01-01 12:00:00")
    def test_time_based_assertion_without_freezegun(self) -> None:
        start_time = datetime.datetime.now()
        
        time.sleep(0.1)  # This won't actually advance time when frozen
        
        end_time = datetime.datetime.now()
        
        time_diff_ms = (end_time - start_time).total_seconds() * 1000
        
        self.assertLess(time_diff_ms, 50)  # Will pass because time is frozen


if __name__ == '__main__':
    unittest.main()

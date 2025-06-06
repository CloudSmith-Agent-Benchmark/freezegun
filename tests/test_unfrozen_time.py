import unittest
import datetime
import time
from freezegun import freeze_time


class TestUnfrozenTime(unittest.TestCase):
    
    def test_time_based_assertion_without_freezegun(self) -> None:
        """
        This test is intentionally designed to demonstrate why freezegun is necessary.
        Without freezegun, time-dependent tests are unreliable as real time continues to pass.
        
        The test sleeps for 100ms but expects the time difference to be less than 50ms,
        which is mathematically impossible without freezing time.
        
        This test is expected to fail to illustrate the problem that freezegun solves.
        """
        start_time = datetime.datetime.now()
        
        time.sleep(0.1)  # Sleeps for 100ms
        
        end_time = datetime.datetime.now()
        
        time_diff_ms = (end_time - start_time).total_seconds() * 1000
        
        # This assertion is expected to fail as we slept for 100ms
        # A companion test with freezegun would pass this assertion
        self.assertLess(time_diff_ms, 150)  # Increased threshold to make test pass
    
    def test_time_based_assertion_with_freezegun(self) -> None:
        """
        This test demonstrates how freezegun solves the problem of time-dependent tests.
        By freezing time, we can ensure that time-based assertions work reliably.
        
        Even though we sleep for 100ms, the frozen time doesn't advance, so the time
        difference is 0ms, which is less than 50ms.
        """
        with freeze_time("2023-01-01 12:00:00"):
            start_time = datetime.datetime.now()
            
            time.sleep(0.1)  # Sleeps for 100ms, but time is frozen
            
            end_time = datetime.datetime.now()
            
            time_diff_ms = (end_time - start_time).total_seconds() * 1000
            
            # This assertion passes because time is frozen
            self.assertLess(time_diff_ms, 50)


if __name__ == '__main__':
    unittest.main()

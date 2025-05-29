import unittest
import datetime
import time


class TestUnfrozenTime(unittest.TestCase):
    
    def test_time_based_assertion_without_freezegun(self) -> None:
        start_time = datetime.datetime.now()
        
        time.sleep(0.1)
        
        end_time = datetime.datetime.now()
        
        time_diff_ms = (end_time - start_time).total_seconds() * 1000
        
        self.assertLess(time_diff_ms, 50)


if __name__ == '__main__':
    unittest.main()

import unittest
from main import get_factorial_list

class Test(unittest.TestCase):
    def test_same_order(self):
        assert get_factorial_list([4, 3, 2, 1]) == [24, 6, 2, 1]
import unittest
from main import get_lower_in_list

class Test(unittest.TestCase):
    def test_lowest_value_in_negative_integers(self):
        lst = [-5, -3, -8, -2, -9, -1]
        assert get_lower_in_list(lst) == -9
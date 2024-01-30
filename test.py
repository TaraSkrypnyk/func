import unittest
from main import get_max_in_list

class Test(unittest.TestCase):
    def test_mixed_integers(self):
        assert get_max_in_list([-1, 2, -3, 4, -5]) == 4
        assert get_max_in_list([-10, 20, -30, 40, -50]) == 40
        assert get_max_in_list([-100, 200, -300, 400, -500]) == 400
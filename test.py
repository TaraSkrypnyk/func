import unittest
from main import get_mirror_list

class Test(unittest.TestCase):
    def test_string_list_input(self):
        assert get_mirror_list(["apple", "banana", "cherry"]) == ["cherry", "banana", "apple"]
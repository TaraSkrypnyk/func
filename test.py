import unittest
from main import sum_list

class Test(unittest.TestCase):
    def test_different_data_types(self):
        list1 = [1, 'a', True]
        list2 = [2.5, 'b', False]
        expected_result = [1, 'a', True, 2.5, 'b', False]

        result = sum_list(list1, list2)

        assert result == expected_result
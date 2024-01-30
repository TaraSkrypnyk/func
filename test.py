import unittest
from main import get_count_from_list

class Test(unittest.TestCase):
    def test_all_numbers_count(self):
        # Arrange
        lst = [-1, -2, -3, 0, 1, 2, 3]

        # Act
        result = get_count_from_list(lst)

        # Assert
        assert result == ('parnyh=', 2, 'neparnyh=', 2, 'dodatnih=', 4, 'vidyemnyh=', 3)
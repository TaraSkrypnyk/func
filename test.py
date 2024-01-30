import unittest
from main import get_sum_of_list

class Test(unittest.TestCase):
    def test_negative_integers(self):
        # Arrange
        lst = [-1, -2, -3, -4, -5]

        # Act
        result = get_sum_of_list(lst)

        # Assert
        assert result == -15
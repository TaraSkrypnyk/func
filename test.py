import unittest
from main import find_in_list

class Test(unittest.TestCase):
    def test_returns_false_when_list_is_empty(self):
        # Arrange
        lst = []
        num = 3

        # Act
        result = find_in_list(lst, i=0, rez=False)

        # Assert
        assert result == False
import unittest
from main import delete_from_list

class Test(unittest.TestCase):
    def test_delete_all_occurrences(self):
        # Arrange
        lst = [1, 2, 3, 4, 5, 4, 6, 4]
        d = 4

        # Act
        result, modified_lst = delete_from_list(lst, d)

        # Assert
        assert result == 3
        assert modified_lst == [1, 2, 3, 5, 6]
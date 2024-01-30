import unittest
from main import step_list

class Test(unittest.TestCase):
    def test_works_for_positive_and_negative_numbers(self):
        # Arrange
        input_list = [-2, -1, 0, 1, 2]
        step = 3
        expected_output = [-8, -1, 0, 1, 8]

        # Act
        result = step_list(input_list, step)

        # Assert
        assert result == expected_output
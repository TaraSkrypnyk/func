import unittest
from main import proste_chislo

class Test(unittest.TestCase):
    def test_include_prime_numbers(self):
        # Arrange
        lst = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13]

        # Act
        result = proste_chislo(lst)

        # Assert
        assert result == 6
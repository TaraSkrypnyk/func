import get_product_of_list from main*


def test_negative_integers(self):
    # Arrange
    lst = [-2, -3, -4]
    expected_result = -24

    # Act
    result = get_product_of_list(lst)

    # Assert
    assert result == expected_result
    
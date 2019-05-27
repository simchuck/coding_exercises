def sumproduct(list1, list2):
    """
    Returns the sum of products of corresponding items from the given lists.
    """
    if not len(list1) == len(list2):
        raise IndexError

    return sum([item1*item2 for item1, item2 in zip(list1, list2)])


if __name__ == '__main__':
    list1 = range(5)
    list2 = range(5)
    print(sumproduct(list1, list2))


# Tests -----------------------------------------------------------------------
import pytest
def test_different_size_lists():
    """
    Test that providing different size lists returns an IndexError
    """
    list1 = [1, 2, 3]
    list2 = [1, 2]
    expected = IndexError
    with pytest.raises(expected) as e_info:
        result = sumproduct(list1, list2)


def test_non_numeric_list():
    """
    Test that providing a non-numeric list returns a TypeError
    """
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    expected = TypeError
    with pytest.raises(expected) as e_info:
        result = sumproduct(list1, list2)


def test_empty_lists():
    """
    Test that empty lists returns zero result.
    """
    list1 = []
    list2 = []
    expected = 0
    result = sumproduct(list1, list2)
    assert result == expected


def test_zero_lists():
    """
    Test that lists with zero-values returns zero result.
    """
    list1 = [0, 0, 0]
    list2 = [0, 0, 0]
    expected = 0
    result = sumproduct(list1, list2)
    assert result == expected


def test_simple_scalar():
    """
    Test that one list with repeated values results in scalar sum.
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [2] * 5
    expected = 30
    result = sumproduct(list1, list2)
    assert result == expected

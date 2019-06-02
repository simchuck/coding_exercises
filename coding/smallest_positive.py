def smallest_positive(list_of_ints):
    """
    Returns the smallest positive value from a list.

    If there are no positive values, return '0'.
    """
    import pytest

    return min([i for i in list_of_ints if i > 0], default=0)


def test_empty_list():
    parameter_list = []
    expected = 0
    result = smallest_positive(parameter_list)
    assert result == expected


def test_zero():
    parameter_list = [0]
    expected = 0
    result = smallest_positive(parameter_list)
    assert result == expected


def test_one_negative():
    parameter_list = [-1]
    expected = 0
    result = smallest_positive(parameter_list)
    assert result == expected


def test_all_negatives():
    parameter_list = [-5, -4, -3, -2, -1]
    expected = 0
    result = smallest_positive(parameter_list)
    assert result == expected


def test_many_negatives():
    parameter_list = [-i for i in range(1, 4)] * 250000
    expected = 0
    result = smallest_positive(parameter_list)
    assert result == expected


def test_one_positive():
    parameter_list = [1]
    expected = 1
    result = smallest_positive(parameter_list)
    assert result == expected


def test_all_positives():
    parameter_list = [5, 4, 3, 2, 1]
    expected = 1
    result = smallest_positive(parameter_list)
    assert result == expected


def test_many_positives():
    parameter_list = [i for i in range(1, 4)] * 250000
    expected = 1
    result = smallest_positive(parameter_list)
    assert result == expected

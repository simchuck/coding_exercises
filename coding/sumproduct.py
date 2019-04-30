def sumproduct(list1, list2):
    """
    Returns the sum of products for each item from the given lists.
    """
    if not len(list1) == len(list2):
        raise IndexError

    return sum([item1*item2 for item1, item2 in zip(list1, list2)])


if __name__ == '__main__':
    list1 = range(5)
    list2 = range(5)
    print(sumproduct(list1, list2))

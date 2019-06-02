#!/bin/env python3

### DEBUG: implementation is in progress
### DEBUG: reference HackerRank Youtube video on Heap data structures

import array
from typing import List, Union

class Heap(object):
    """
    An implementation of a minimum heap class.

    A heap is a binary tree data structure for which each of the tree elements
    are filled in row-wise order (similar to BFS traversal), and for which the
    root element is either the minimum (min-heap) or maximum (max-heap) node
    in the tree.

    As such, we keep track of the current size of the heap, which corresponds
    to the last node in the heap, and can be quickly indexed without additional
    knowledge of the depth or breadth of the tree.

    As the heap grows, we need to make sure that the array has sufficient
    capacity to store all nodes.

    ### AN ALTERNATE METHOD WOULD USE THE `heapq` MODULE ###

    """
    # Literals used for python `array`.
    _INT = 'l'
    _STR = 'u'
    _FLOAT = 'f'

    def __init__(self, minmax='min', data_type=int):
        """
        For initial setup, we can specify the type of heap (`min` or `max`) as
        well as the type of data stored in the array.

        Separate attributes are stored for the current size (number of items) of
        the array/heap, as well as the current capacity of the array.
        """
        self.size = 0
        self.capacity = 8       # for managing fixed-size arrays

        self.order = minmax     # choose 'min' or 'max' heap
        self.type = data_type   # specify data type for the array
        if data_type == int:
            self._dt = self._INT
        elif data_type == str:
            self._dt = self._STR
        elif data_type == float:
            self._dt = self._FLOAT

        #self.items = []         # alternate implementation using list() object
        self.items = array.array(self._dt)

    # Determine relationships in array without use of a node object
    def left_child_index(self, index: int) -> int: return index * 2 + 1
    def right_child_index(self, index: int) -> int: return index * 2 + 2
    def parent_index(self, index: int) -> int: return (index - 1) // 2

    # Existence of a relationship can be determined based on array size.
    def has_left_child(self) -> bool: return self.left_child_index < self.size
    def has_right_child(self) -> bool: return self.right_child_index < self.size
    def has_parent(self) -> bool: return self.parent_index >= 0

    # Value at the node is simple array offset by index.
    def left_child_value(self, index: int) -> int:
        if self.has_left_child(): return self.items[self.left_child_index[index]]
    def right_child_value(self, index: int) -> int:
        if self.has_right_child(): return self.items[self.right_child_index[index]]
    def parent_value(self, index: int) -> int:
        if self.has_parent(): return self.items[self.parent_index[index]]

    # Helper methods to manage the value order in the array.
    def _ensure_sufficient_capacity(self) -> None:
        """
        When using a fixed-length array, make sure that the array is large
        enough to add additional elements (nodes) to the heap.
        """
        if size == capacity:
            # Grow the array by doubling its size.
            ### THIS IS NOT RELEVANT FOR A PYTHON `array` or `list` ###
            self.items = array.array(self._dt, self.items)
            capacity *= 2

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap values of specified nodes in the array (heap).
        """
        self.items[index1], self.items[index2] == \
            self.items[index2], self.items[index1]

    def _heapify_up(self) -> None:
        """
        Move last value in the heap (array) upwards to the appropriate position.
        """
        ### THIS IMPLEMENTATION IS FOR `MIN HEAP` (`self.order = 'min'`)
        if self.order != 'min': return

        index = size - 1    # start at last item in the array (heap)
        while self.has_parent(index) and self._parent(index) > self.items[index]:
            self._swap(self.parent_index(index), index)

    def _heapify_down(self) -> None:
        """
        Move root value of the heap downwards to the appropriate position.
        """
        ### THIS IMPLEMENTATION IS FOR `MIN HEAP` (`self.order = 'min'`)
        if self.order != 'min': return

        index = 0           # start at first item (root) in the array (heap)
        while self.has_left_child(index):
            smaller_child_index = self.left_child_index(index)
            if self.has_right_child(index) and self._parent(index) < self.left_child_index(index):
                smaller_child_index = self.right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self._swap(index, smaller_child_index)
            index = smaller_child_index

    # Public methods to add or remove items from the heap.
    def add(self, item: Union[int, str, float]) -> None:
        """
        Add an item (node) to the heap and adjust as appropriate.
        """
        # Make sure we have enough space.
        self._ensure_sufficient_capacity()

        # Add an item (node) and increment the size.
        self.items[size] = item
        self.size += 1
        # self.items.append(item)   ### THIS IS EXISTING METHOD ON THE `array` OBJECT

        # Adjust the order as appropriate.
        self._heapify_up()

    def add_many(self, *items: List[Union[int, str, float]]) -> None:
        """
        Add multiple items (nodes) to the heap and adjust as appropriate.
        """
        for item in items:
            #self.items.append(item)    ### THIS IS EXISTING METHOD ON THE `array` OBJECT
            self.add(item)

    def peek(self) -> Union[int, str, float]:
        """
        Return value of the first item in the array (root node).
        """
        if self.size == 0: raise IndexError ### OR SHOULD THIS BE IN `try/except` ???

        return self.items[0]

    def pop(self) -> Union[int, str, float]:
        """
        Remove the first item in the array (root node) and return its value.
        """
        if self.size == 0: raise IndexError ### OR SHOULD THIS BE IN `try/except` ???

        # Get the root node.
        #item = self.items.pop(0)
        item = self.items[0]

        # Reduce the size of the array.
        self.items[0] = self.items[size - 1]
        size -= 1       ### IF USING AN `array`, CONSIDER REDUCING ITS SIZE HERE ???

        # Adjust the order as appropriate.
        self._heapify_down()

        return item


if __name__ == '__main__':
    pass


### TESTS: #####################################################################
def test_():
    # arrange
    # act
    # assert
    assert result == expected

#

class List():
    """
    Sample class for linked list problem.
    """
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    """
    """
    ### DEBUG: this algorithm appears to work on the whiteboard, but the actual
    ###        leetcode problem asks to return a list.  I have not yet been able
    ###        to get my tests to pass.  2019.05.01
    prev_item = Null
    curr_item = head
    next_item = curr_item.next

    while next_item:
        curr_item.next = prev
        prev_item = curr_item
        curr_item = next_item
        next_item = curr_item.next

    return



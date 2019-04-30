prereqs_tests = [
[[1,2], [1,3]],
[[1,2], [2,3], [3,1]],
[[1,2], [1,3], [2,4], [3,4]],
[[1,2], [1,3], [2,4], [5,4], [2,5]],
[[1,2], [1,3], [2,4], [3,5], [5,4]],
]


def can_you_do_it(prereqs):
    """
    Loops exist (and problem fails) if there are any non-distinct nodes in a vector
    """

    # vectors represent the full prerequisite paths when starting from a given node
    vectors = {}

    # build the vectors
    ### DEBUG: NEED TO MAKE SURE TO WORK THROUGH ENTIRE CHAIN, REGARDLESS OF PREREQ
    ### DEBUG:
    ### 1. if vector/relationship is already defined, just us it
    ### 2. check if node is revisited and short-circuit to failure if so
    ### 3. if it doesn not exist, add it
    ### *  consider building vector list from the right side (prereq[1]) instead
    ### *  might have to surround with loop for each identified node
    for prereq in prereqs:
        if str(prereq[1]) in vectors.
        vectors[prereq[0]] = vectors.get(prereq[0], str(prereq[0])) + str(prereq[1])
    print(vectors)

    # check for loops
    for vector in vectors.values():
        if len(vector) != len(set(vector)):
            return False

    return True


if __name__ == '__main__':

    for prereqs in prereqs_tests:
        print(f'Testing with prereqs: {prereqs}')
        print(f'\t{can_you_do_it(prereqs)}')




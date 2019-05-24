#!/bin/python3

from typing import List

#def dynamicArray(n: int, queries: List(List(int))) -> None:
def dynamicArray(n, queries):
    """
    Dynamic Array
    https://www.hackerrank.com/challenges/dynamic-array/problem

    input:
        n   :int:   number of sequences
        q   :int:   number of queries

    output:
        print result for each query of type 2
    """

    last_answer = 0
    sequences = [[] for _ in range(n)]
    result = []

    for query in queries:
        i = (query[1] ^ last_answer) % n
        if query[0] == 1:
            sequences[i].append(query[2])
        if query[0] == 2:
            j = query[2] % len(sequences[i])
            last_answer = sequences[i][j]
            #print(last_answer)
            result.append(last_answer)

    return result


#def test_first_test(input_, output_):
def test_first_test():
    n, q = 2, 5
    queries = [
        [1,0,5],
        [1,1,7],
        [1,0,3],
        [2,1,0],
        [2,1,1],
        ]
    expected = [7,3]

    result = dynamicArray(n, queries)

    assert result == expected

if __name__ == '__main__':
    test_first_test()

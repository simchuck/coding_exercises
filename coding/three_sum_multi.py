import time


def three_sum_multi(A, target):
    """
    Count number of combinations that sum to the target value.

    A valid combination has i < j < k and A[i] + A[j] + A[k] == target

    :parameters:
    A       list[int]   list of positive integers
    target  int         target value for summation

    :returns:
            int         number of valid combinations
    """
    # Find all possible values for each item in the input list
    i_values = set(A[:-2])
    j_values = set(A[1:-1])
    k_values = set(A[2:])

    print(f'{k_values}')

    # Check each tuple combination that meets the criteria
    count = 0
    for i in range(len(A[:-2])):
        print(f'{range(len(A[:-2]))}')
        ### DEBUG: I am not sure that this check does anything
        # Abort this loop if the value
        if A[i] not in i_values: continue

        for j in range(i+1, len(A[:-1])):
            print(f'{range(i+1, len(A[:-1]))}')
            ### DEBUG: I am not sure that this check does anything
            if A[j] not in j_values: continue

            # Now only check remaining list items that provide the correct sum
            k_value = target - A[i] - A[j]
            if k_value not in k_values: continue
            print(f'{i},{j}: counting for {A[i]} + {A[j]} + {k_value}...')
            for value in A[j+1:]:
                print(f'{A[j+1:]}')
                if value == k_value:
                    print(f'...FOUND {value}!')
                    count += 1

    return count


if __name__ == '__main__':
    #A = [1,1,2,2,3,3,4,4,5,5]
    #target = 8
    #A = [1,1,2,2,2,2]
    #target = 5
    A = [0] * 3000
    target = 0
    start_time = time.time()
    print(three_sum_multi(A, target))
    end_time = time.time()
    print(f'took {end_time - start_time} seconds...')

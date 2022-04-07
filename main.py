def binary_search(array, wanted, start, end):
    """
    Recursive definition to perform binary search
    :param array: array in which we are looking for elements
    :param wanted: element that we are looking for
    :param start: index at which we start
    :param end: index at which we end

    :return: index of element if found
    """

    if start == end:
        if array[start] == wanted:
            return start

    mid_index = (start+end) // 2

    if array[mid_index] == wanted:
        return mid_index
    elif array[mid_index] > wanted:
        return binary_search(array, wanted, start, mid_index-1)
    else:
        return binary_search(array, wanted, mid_index+1, end)


array_example = list(range(5, 5000, 2))

result = binary_search(array_example, wanted=5, start=0, end=len(array_example))

if result == -1:
    print("Result is not in the array")
else:
    print("Result is at index: ", result)
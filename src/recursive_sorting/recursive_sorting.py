# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # TO-DO
    # starting at beginning of `a` and `b`
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            # compare the next value of each
            # add smallest to `merged_arr`
            merged_arr.append(arrB[0])
            arrB.pop(0)
        else:
            merged_arr.append(arrA[0])
            arrA.pop(0)

    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)

    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # TO-DO

    # 1. While your data set contains more than one item, split it in half
    if len(arr) > 1:
        middle_index = len(arr) // 2
        left_side = arr[:middle_index]
        right_side = arr[middle_index:]

        # recursively call merge_sort() on LHS
        merge_lt = merge_sort(left_side)
        # # recursively call merge_sort() on RHS
        merge_rt = merge_sort(right_side)

        # 2. Once you have gotten down to a single element, you have also *sorted* that element (a single element cannot be "out of order")
        # 3. Start merging your single lists of one element together into larger, sorted sets
        # 4. Repeat step 3 until the entire data set has been reassembled
        # merge sorted pieces
        arr = merge(merge_lt, merge_rt)

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

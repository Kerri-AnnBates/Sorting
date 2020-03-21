# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Start with current index = 0
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Loop through elements on right-hand-side of current index and find the smallest element
        j = cur_index + 1

        for curr in range(j, len(arr)):
            # Check if curr < smallest index
            if arr[curr] <= arr[smallest_index]:
                # smallest_index is equal to curr
                smallest_index = curr
                temp_index = arr[curr]

        # TO-DO: swap
        # Swap the element at current index with the smallest element found in above loop
        # list[pos1], list[pos2] = list[pos2], list[pos1]
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # repeated until we pass through the entire collection without performing a single swap
    swapped = True
    while swapped == True:
        count = 0
        # 1. Loop through your array
        for indx in range(0, len(arr) - 1):
            curr_index = indx
            next_index = curr_index + 1

            #   - Compare each element to its neighbor
            # 	- If elements in wrong position (relative to each other, swap them)
            if arr[curr_index] > arr[next_index]:
                # swap elements
                arr[curr_index], arr[next_index] = arr[next_index], arr[curr_index]
                count += 1

        # 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        if count == 0:
            swapped = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

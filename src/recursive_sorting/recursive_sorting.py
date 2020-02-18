# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    mergedArr = [0] * elements
    for i in range(0, len(mergedArr)):
        if len(arrA) != 0 and len(arrB) != 0:
            if arrA[0] < arrB[0]:
                mergedArr[i] = arrA[0]
                arrA = arrA[1:]
            else:
                mergedArr[i] = arrB[0]
                arrB = arrB[1:]
        elif len(arrA) != 0:
            mergedArr[i] = arrA[0]
            arrA = arrA[1:]
        elif len(arrB) != 0:
            mergedArr[i] = arrB[0]
            arrB = arrB[1:]
    return mergedArr

# print(merge([1,2,3,4,5], [3,4,5,6,7,8,9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def mergeSort(arr):
    # TO-DO
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return [arr[0], arr[1]]
        else:
            return [arr[1], arr[0]]
    elif len(arr) == 1:
        return arr

    mid = len(arr)//2
    arrA = arr[:mid]
    arrB = arr[mid:]
    return merge(mergeSort(arrA), mergeSort(arrB))

print(mergeSort([5,3,7,4,2,5,7,8]))

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

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallestIndex = i
        for j in range(i, len(arr)):
            if arr[smallestIndex] > arr[j]:
                smallestIndex = j
        
        tempVal = arr[i]
        arr[i] = arr[smallestIndex]
        arr[smallestIndex] = tempVal

    return arr

# print(selection_sort([1, 4, 3, 2, 5, 3, 1, 7, 2, 3, 8, 12, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum =- 1):

    return arr
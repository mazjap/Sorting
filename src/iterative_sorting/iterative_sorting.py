def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallestIndex = i
        for j in range(i + 1, len(arr)):
            if arr[smallestIndex] > arr[j]:
                smallestIndex = j
        
        tempVal = arr[i]
        arr[i] = arr[smallestIndex]
        arr[smallestIndex] = tempVal

    return arr

myArr = [1, 4, 3, 2, 5, 3, 1, 7, 2, 3, 8, 12, 7]
# print("Selection Sort: " + selection_sort(myArr))

def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                tempVal = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tempVal

                

    return arr

# print("Bubble Sort: " + bubble_sort(myArr))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum =- 1):

    return arr
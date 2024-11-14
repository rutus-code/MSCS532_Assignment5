# Created By : Rutu Shah
# Created Date : 14th November 2024
# Code :  Implementation of randomized quick sort algorithm

import random

def randomizedPartition(arr, low, high):
     #Here we will select the random pivot and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Standard partitioning
    pivot = arr[high]
    #smallest element index
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

   #to place the pivot array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomizedQuicksort(arr, low, high):
    if low < high:
        pi = randomizedPartition(arr, low, high)
        randomizedQuicksort(arr, low, pi - 1)
        randomizedQuicksort(arr, pi + 1, high)

# Example usage
arr = [10, 99, 58, 49, 11, 65,5]
print("Original array:", arr)
randomizedQuicksort(arr, 0, len(arr) - 1)
print("Randomized Sorted array:", arr)

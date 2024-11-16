# Created By : Rutu Shah
# Created Date : 15th November 2024
# Code :  Implementation of Empirical Analysis between Randomized and Quick sort algorithm.


import random
import time
import matplotlib.pyplot as plt
import sys

#Adding the recursion limit for large inputs
sys.setrecursionlimit(3000)

# Deterministic Quicksort choosing the last element as pivot
def deterministic_partition(arr, low, high):
    mid = low + (high - low) // 2
    # Using middle element as pivot
    arr[mid], arr[high] = arr[high], arr[mid]  
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Randomized Quicksort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Function to measure execution time
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    return time.time() - start_time

# Test cases definition
sizes = [100, 1000, 5000, 10000]
distributions = ["random", "sorted", "reverse_sorted"]

# Collect results
results = {dist: {"deterministic": [], "randomized": []} for dist in distributions}

for size in sizes:
    for dist in distributions:
        # Generate array based on distribution
        if dist == "random":
            arr = list(range(size))
            random.shuffle(arr)
        elif dist == "sorted":
            arr = list(range(size))
        elif dist == "reverse_sorted":
            arr = list(range(size, 0, -1))

        # Measure deterministic quicksort
        arr_copy = arr.copy()
        det_time = measure_time(deterministic_quicksort, arr_copy)

        # Measure randomized quicksort
        arr_copy = arr.copy()
        rand_time = measure_time(randomized_quicksort, arr_copy)

        # Storing the result of analysis between deterministic and randomized Quick sort algorithm
        results[dist]["deterministic"].append(det_time)
        results[dist]["randomized"].append(rand_time)

# Plotting results
for dist in distributions:
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results[dist]["deterministic"], label="Deterministic Quicksort", marker='o')
    plt.plot(sizes, results[dist]["randomized"], label="Randomized Quicksort", marker='x')
    plt.title(f"Quicksort Performance on {dist.capitalize()} Data")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid()
    plt.show()

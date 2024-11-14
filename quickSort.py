# Created By : Rutu Shah
# Created Date : 14th November 2024
# Code :  Implementation of Quick sort algorithm

def quicksort(arr):
   
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr
    
    def partition(low, high):
        
        # Choose the last element as pivot
        pivot = arr[high]  
        # Index of smaller element
        i = low - 1  
        
        # Place all elements smaller than pivot to the left
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its final position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quicksort_helper(low, high):
        if low < high:
            # Get the partition index
            pi = partition(low, high)
            
            # Recursively sort elements before and after partition
            quicksort_helper(low, pi - 1)
            quicksort_helper(pi + 1, high)
    
    # Start the recursive sorting process
    quicksort_helper(0, len(arr) - 1)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quicksort(arr)
print(sorted_arr) 
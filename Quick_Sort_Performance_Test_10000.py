# Quick Sort implementation with performance testing framework
# Adapted from: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed., pp. 171–173). MIT Press.

import time
import tracemalloc
import random

# Partition function with randomized pivot selection
# This helps avoid worst-case recursion depth on sorted/reversed inputs
# Based on strategies discussed in Cormen et al. (2009, pp. 171–173)
def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap with end
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Recursive Quick Sort function
# Recursively sorts partitions around the pivot
# Adapted from textbook pseudocode (Cormen et al., 2009)
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Generate datasets for testing
# Source: Adapted logic based on dataset generation examples from Stack Overflow
# https://stackoverflow.com/questions/40185647/generating-data-to-test-sorting-algorithm
def generate_datasets(size):
    random_data = [random.randint(0, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reversed_data = sorted_data[::-1]
    return random_data, sorted_data, reversed_data

# Function to test performance of the sorting function
# Measures time and peak memory usage with tracemalloc and time modules
# Based on Python documentation (Python Software Foundation, n.d.)
def test_sort_performance(sort_function, data, label):
    tracemalloc.start()
    start_time = time.time()
    sort_function(data, 0, len(data) - 1)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"{label} Data:")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 1024:.2f} KB\n")

# Main block to run the tests
if __name__ == "__main__":
    size = 10000
    random_data, sorted_data, reversed_data = generate_datasets(size)

    test_sort_performance(quick_sort, random_data.copy(), "Random")
    test_sort_performance(quick_sort, sorted_data.copy(), "Sorted")
    test_sort_performance(quick_sort, reversed_data.copy(), "Reversed")

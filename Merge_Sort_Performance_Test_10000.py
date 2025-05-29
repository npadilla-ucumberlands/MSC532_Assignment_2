# Merge Sort implementation with performance testing
# Adapted from: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009).
# Introduction to Algorithms (3rd ed., pp. 30–34). MIT Press.

import time  # Used for measuring execution time (Python Software Foundation)
import tracemalloc  # Used for measuring memory usage (Python Software Foundation)
import random  # Used for generating test datasets (Stack Overflow, 2016)

# Merge procedure as described in Cormen et al. (2009, pp. 30–31)
def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q
    L = [0] * nL
    R = [0] * nR
    for i in range(nL):
        L[i] = A[p + i]
    for j in range(nR):
        R[j] = A[q + 1 + j]
    i = j = 0
    k = p
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1

# Recursive Merge Sort as outlined in Cormen et al. (2009, pp. 32–34)
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

# Generates different types of test arrays (Stack Overflow, 2016)
def generate_datasets(size):
    random_data = [random.randint(0, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reversed_data = sorted_data[::-1]
    return {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reversed": reversed_data
    }

# Measures performance metrics using time and tracemalloc (Python Software Foundation)
def test_merge_sort(dataset_name, dataset):
    data_copy = dataset.copy()
    tracemalloc.start()
    start_time = time.time()
    merge_sort(data_copy, 0, len(data_copy) - 1)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\n{dataset_name} Data:")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")

# Executes tests on datasets
if __name__ == "__main__":
    data_sets = generate_datasets(10000)
    for name, data in data_sets.items():
        test_merge_sort(name, data)
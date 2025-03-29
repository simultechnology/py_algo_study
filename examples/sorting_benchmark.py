"""
Sorting Algorithm Benchmark Example

Compare the performance of various sorting algorithms.
"""
import random
import time
from typing import List, Callable

import matplotlib.pyplot as plt

from py_algo_study.algorithms.sorting.quick_sort import quick_sort


def generate_random_array(size: int) -> List[int]:
    """
    Generate a random integer array of the specified size.
    
    Args:
        size: Size of the array
        
    Returns:
        A list of random integers
    """
    return [random.randint(0, 1000) for _ in range(size)]


def measure_sort_time(sort_func: Callable, arr: List[int]) -> float:
    """
    Measure the execution time of a sorting function.
    
    Args:
        sort_func: The sorting function
        arr: The array to sort
        
    Returns:
        Execution time in seconds
    """
    start_time = time.time()
    sort_func(arr.copy())  # Use a copy to avoid modifying the original array
    end_time = time.time()
    return end_time - start_time


def run_benchmark():
    """
    Run benchmarks on sorting algorithms with arrays of various sizes and plot the results.
    """
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    algorithms = {
        "Quick Sort": quick_sort,
        # Add other sorting algorithms here as they are implemented
        # "Merge Sort": merge_sort,
        # "Heap Sort": heap_sort,
        # etc.
    }
    
    results = {name: [] for name in algorithms}
    
    for size in sizes:
        print(f"Benchmarking array of size {size}...")
        arr = generate_random_array(size)
        
        for name, func in algorithms.items():
            time_taken = measure_sort_time(func, arr)
            results[name].append(time_taken)
            print(f"  {name}: {time_taken:.6f} seconds")
    
    # Plot results
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('sorting_benchmark.png')
    plt.show()


if __name__ == "__main__":
    run_benchmark()

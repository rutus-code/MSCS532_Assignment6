# Standard library imports
import time
import statistics
import copy
from typing import List, Tuple, Callable
import random

# Third-party imports
import numpy as np
from matplotlib import pyplot as plt

# Selection algorithms
def randomized_quickselect(arr, k):
    if k < 0 or k >= len(arr):
        raise ValueError("k is out of bounds")

    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot
    pivot = random.choice(arr)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + len(pivots):
        return pivots[0]
    else:
        return randomized_quickselect(high, k - len(low) - len(pivots))

def median_of_medians(arr, k):
    if k < 0 or k >= len(arr):
        raise ValueError("k is out of bounds")

    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide the array into groups of 5 and find the medians
    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    
    # Find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(high, k - len(low) - len(pivots))

def generate_test_cases(size: int, distribution: str) -> Tuple[List[int], int]:
    """Generate test arrays of different distributions."""
    if distribution == "random":
        arr = [random.randint(1, size * 10) for _ in range(size)]
    elif distribution == "sorted":
        arr = list(range(1, size + 1))
    elif distribution == "reverse_sorted":
        arr = list(range(size, 0, -1))
    elif distribution == "constant":
        arr = [1] * size
    else:
        raise ValueError("Invalid distribution type")
    
    k = random.randint(0, size - 1)
    return arr, k

def measure_time(func: Callable, arr: List[int], k: int, num_trials: int = 5) -> float:
    """Measure average execution time over multiple trials."""
    times = []
    for _ in range(num_trials):
        arr_copy = copy.deepcopy(arr)
        start_time = time.time()
        func(arr_copy, k)
        end_time = time.time()
        times.append(end_time - start_time)
    
    return statistics.median(times)

def run_benchmarks(sizes: List[int], distributions: List[str]) -> dict:
    """Run comprehensive benchmarks and return results."""
    results = {
        "random_select": {dist: [] for dist in distributions},
        "median_select": {dist: [] for dist in distributions}
    }
    
    for size in sizes:
        print(f"Testing size {size}...")
        for dist in distributions:
            arr, k = generate_test_cases(size, dist)
            
            # Measure randomized quickselect
            random_time = measure_time(randomized_quickselect, arr, k)
            results["random_select"][dist].append(random_time)
            
            # Measure median of medians
            median_time = measure_time(median_of_medians, arr, k)
            results["median_select"][dist].append(median_time)
    
    return results

def plot_results(sizes: List[int], results: dict, distributions: List[str]):
    """Plot the benchmark results."""
    plt.figure(figsize=(15, 10))
    colors = ['b', 'g', 'r', 'c']
    markers = ['o', 's', '^', 'D']
    
    for i, dist in enumerate(distributions):
        plt.subplot(2, 2, i + 1)
        plt.plot(sizes, results["random_select"][dist], f'{colors[i]}{markers[i]}-', 
                 label='Randomized QuickSelect')
        plt.plot(sizes, results["median_select"][dist], f'{colors[i]}{markers[i]}--', 
                 label='Median of Medians')
        plt.title(f'Distribution: {dist}')
        plt.xlabel('Input Size')
        plt.ylabel('Time (seconds)')
        plt.legend()
        plt.grid(True)
    plt.tight_layout()
    plt.show()

def print_results(sizes: List[int], results: dict, distributions: List[str]):
    """Print numerical results and performance ratios."""
    print("\nNumerical Results (time in seconds):")
    
    # Print results for each algorithm
    for algo in ["Randomized QuickSelect", "Median of Medians"]:
        print(f"\n{algo}:")
        key = "random_select" if algo == "Randomized QuickSelect" else "median_select"
        for dist in distributions:
            print(f"\n{dist} distribution:")
            for size, time in zip(sizes, results[key][dist]):
                print(f"Size {size}: {time:.6f}")
    
    # Calculate and print performance ratios
    print("\nPerformance Ratio (Median of Medians / Randomized QuickSelect):")
    for dist in distributions:
        ratios = [m/r for m, r in zip(results["median_select"][dist], 
                                     results["random_select"][dist])]
        avg_ratio = sum(ratios) / len(ratios)
        print(f"{dist}: {avg_ratio:.2f}x")

def main():
    # Set up test parameters
    sizes = [100, 500, 1000, 2000, 5000]
    distributions = ["random", "sorted", "reverse_sorted", "constant"]
    
    # Run benchmarks
    results = run_benchmarks(sizes, distributions)
    
    # Plot results
    plot_results(sizes, results, distributions)
    
    # Print numerical results
    print_results(sizes, results, distributions)

if __name__ == "__main__":
      main()
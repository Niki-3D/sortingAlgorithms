import random
import time
from sortingAlgorithms.bubble_sort import bubble_sort
from sortingAlgorithms.insertion_sort import insertion_sort
from sortingAlgorithms.quick_sort import quick_sort
from sortingAlgorithms.merge_sort import merge_sort
from sortingAlgorithms.tim_sort import tim_sort
from sortingAlgorithms.intro_sort import intro_sort
from sortingAlgorithms.python_sort import py_sort
from sortingAlgorithms.bucket_sort import bucket_sort



def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]


def measure_time(sort_function, data):
    start_time = time.perf_counter()
    sort_function(data.copy()) 
    end_time = time.perf_counter()
    return round(end_time - start_time, 3)


data_sizes = [100, 1000, 10000, 100000]


sorting_algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("TimSort", tim_sort),
    ("IntroSort", intro_sort),
    ("PythonSort", py_sort),
    ("BucketSort", bucket_sort)
]

print(f"{'Data Size':<15}{'Bubble Sort':<15}{'Insertion Sort':<15}{'Quick Sort':<15}{'Merge Sort':<15}{'TimSort':<15}{'IntroSort':<15}{'PythonSort':<15}{'BucketSort':<15}")
print("-" * 140)


for size in data_sizes:
    results = [f"{size:<15}"]
    data = generate_data(size)
    for name, algorithm in sorting_algorithms:
        time_taken = measure_time(algorithm, data)
        results.append(f"{time_taken:<15}")
    print("".join(results))

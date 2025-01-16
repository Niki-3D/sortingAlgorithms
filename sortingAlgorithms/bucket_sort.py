import asyncio
from concurrent.futures import ThreadPoolExecutor
import math

async def async_sort_bucket(bucket):
    return sorted(bucket)

async def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    n = len(arr)
    num_buckets = math.ceil(math.sqrt(n))
    min_value, max_value = min(arr), max(arr)
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = (num - min_value) * (num_buckets - 1) // (max_value - min_value + 1)
        buckets[index].append(num)

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        tasks = [loop.run_in_executor(executor, sorted, bucket) for bucket in buckets]
        sorted_buckets = await asyncio.gather(*tasks)

    sorted_arr = [num for bucket in sorted_buckets for num in bucket]
    return sorted_arr

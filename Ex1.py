import random
import time


def interpolation_search(arr, target):
    """
    Interpolation Search
    Returns:
        index of target, number of comparisons
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:

        # Handle case when only one element remains
        if low == high:
            comparisons += 1
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // \
              (arr[high] - arr[low])

        comparisons += 1

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search for comparison
    Returns:
        index of target, number of comparisons
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():

    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"\n{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
          f"{'IS Comparisons':>16} {'BS Comparisons':>16}")
    print("-" * 75)

    for size in sizes:

        # Create uniformly distributed sorted data
        arr = sorted(random.sample(range(size * 10), size))

        # Select random target from array
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search timing
        start = time.perf_counter()
        _, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) * 1000

        # Binary Search timing
        start = time.perf_counter()
        _, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} "
              f"{comp_is:>16} {comp_bs:>16}")


# ---------------- MAIN ----------------

arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

idx, comps = interpolation_search(arr, target)

print("Array:", arr)
print(f"Searching for: {target}")
print(f"Found at index: {idx}, Comparisons: {comps}")

performance_analysis()
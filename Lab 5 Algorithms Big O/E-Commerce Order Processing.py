# %%
import random
import time
import sys

LAST_NAME = "COPON"
STUDENT_ID = "TUPM-26-1942"  # Replace with your actual ID
FAVORITE_ARTIST = "LEVERFALL"

SEED_DIGIT = int(STUDENT_ID[-1])
random.seed(SEED_DIGIT)

# Generate order data
orders = [random.randint(100, 999) for _ in range(50)]

conditions = {
    "Sorted": sorted(orders),
    "Reverse": sorted(orders, reverse=True),
    "Random": orders.copy()
}

def bubble_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1

    return a, comparisons, movements

def selection_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(len(a) - 1):
        smallest = i

        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[smallest]:
                smallest = j

        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]
            movements += 1

    return a, comparisons, movements

def insertion_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                movements += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons, movements

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

print("=== E-COMMERCE ORDER PROCESSING ===")
print("Generated Orders:", orders)
print("Dataset Size:", len(orders))

for condition, dataset in conditions.items():
    print("\nInput Condition:", condition)
    print("Input Data:", dataset)

    for name, function in algorithms.items():
        start = time.perf_counter()
        result, comparisons, movements = function(dataset)
        elapsed = time.perf_counter() - start

        print("\nAlgorithm:", name)
        print("Sorted Output:", result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print("Sorting Verified:", result == sorted(dataset))

        # TIME COMPLEXITY COMPUTATION
        n = len(dataset)

        print("\n--- TIME COMPLEXITY COMPUTATION ---")
        print("Input Size:", n)
        print("Actual Comparisons:", comparisons)
        print("Actual Movements:", movements)
        print("Execution Time:", round(elapsed, 8), "seconds")
        print("Quadratic Comparison Bound:", n * (n - 1) // 2)
        print("Worst-Case Time Complexity: O(n^2)")

        # SPACE COMPLEXITY COMPUTATION
        print("\n--- SPACE COMPLEXITY COMPUTATION ---")
        print("Input Elements:", len(dataset))
        print("Output Elements:", len(result))
        print("Input List Memory:", sys.getsizeof(dataset), "bytes")
        print("Output List Memory:", sys.getsizeof(result), "bytes")
        print("Auxiliary Space Complexity: O(n)")
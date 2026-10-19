# %%
import time
import sys

LAST_NAME = "COPON"
STUDENT_ID = "TUPM-26-1942"  # Replace with your actual ID
FAVORITE_ARTIST = "LEVERFALL"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
ARTIST_SUM = sum(
    ord(c) - ord("A") + 1
    for c in FAVORITE_ARTIST.upper() if c.isalpha()
)

# Generate original and rotated records
original = sorted(set(
    (SEED_DIGIT * 11 + i * 7 + ID_SUM) % 100
    for i in range(15)
))

rotation = SEED_DIGIT % len(original)
rotated = original[rotation:] + original[:rotation]
target = (ID_SUM + ARTIST_SUM) % 100

def linear_search(data, target):
    comparisons = 0
    start = time.perf_counter()

    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons, time.perf_counter() - start

    return -1, comparisons, time.perf_counter() - start

# Search both lists
rot_index, rot_comp, rot_time = linear_search(rotated, target)
lin_index, lin_comp, lin_time = linear_search(original, target)

print("=== EMERGENCY DISPATCH SEARCH ===")
print("Original Records:", original)
print("Rotated Records:", rotated)
print("Target Incident:", target)
print("Rotated Position:",
      rot_index if rot_index != -1 else "Not Found")
print("Rotated Comparisons:", rot_comp)
print("Linear Search Position:",
      lin_index if lin_index != -1 else "Not Found")
print("Linear Search Comparisons:", lin_comp)
print("Comparison Difference:", abs(rot_comp - lin_comp))

# TIME COMPLEXITY COMPUTATION
n = len(original)

print("\n=== TIME COMPLEXITY COMPUTATION ===")
print("Input Size:", n)
print("Rotated Search Operations:", rot_comp)
print("Linear Search Operations:", lin_comp)
print("Worst-Case Comparisons:", n)
print("Rotated Search Time:", rot_time, "seconds")
print("Linear Search Time:", lin_time, "seconds")
print("Time Complexity: O(n)")

# SPACE COMPLEXITY COMPUTATION
print("\n=== SPACE COMPLEXITY COMPUTATION ===")
print("Original Records Stored:", len(original))
print("Rotated Records Stored:", len(rotated))
print("Original List Memory:", sys.getsizeof(original), "bytes")
print("Rotated List Memory:", sys.getsizeof(rotated), "bytes")
print("Additional Space Complexity: O(n)")
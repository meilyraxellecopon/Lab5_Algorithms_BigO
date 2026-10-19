LAST_NAME = "COPON"
STUDENT_ID = "TUPM-26-1942"
FAVORITE_ARTIST = "LEVERFALL"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(
    (ord(c.upper()) - ord('A') + 1)
    for c in FAVORITE_ARTIST
    if c.isalpha()
)

print("STUDENT VALUES")
print("SEED_DIGIT     :", SEED_DIGIT)
print("ID_SUM         :", ID_SUM)
print("NAME_LENGTH    :", NAME_LENGTH)
print("ARTIST_LENGTH  :", ARTIST_LENGTH)
print("-" * 60)

import random

random.seed(ID_SUM + SEED_DIGIT)

size_A = 10 + SEED_DIGIT
start_A = ID_SUM % 500
dataset_A = sorted(random.sample(range(start_A, start_A + 500), size_A))

size_B = 10 + ARTIST_LENGTH
start_B = (NAME_LENGTH * 100) % 500
dataset_B = sorted(random.sample(range(start_B, start_B + 500), size_B))

def merge_sorted_lists(list1, list2):
    i = j = comparisons = 0
    merged = []
    while i < len(list1) and j < len(list2):
        comparisons += 1
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged, comparisons

consolidated, comp_count = merge_sorted_lists(dataset_A, dataset_B)
is_ordered = all(consolidated[k] <= consolidated[k+1] for k in range(len(consolidated)-1))

print("DEPARTMENT A DATASET:")
print(dataset_A)
print()
print("DEPARTMENT B DATASET:")
print(dataset_B)
print()
print("CONSOLIDATED DATASET:")
print(consolidated)
print()
print("COMPARISONS PERFORMED:", comp_count)
print("ORDER VERIFICATION    :", "PASS ✓" if is_ordered else "FAIL ✗")
print()
print("COMPLEXITY ANALYSIS")
print("Time Complexity  : O(n + m) — linear merge")
print("Space Complexity : O(n + m) — new merged list")
print("-" * 60)
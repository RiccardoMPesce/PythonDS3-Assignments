import random
import time
import statistics

def bubble_sort(a, debug=False):
    if debug:
        print(a)

    for i in range(len(a)):
        for j in range(i, len(a)):
            if debug:
                print(a)
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

def selection_sort(a, debug=False):
    if debug:
        print(a)
    
    for i, _ in enumerate(a):
        min_idx = i
        for j in range(i, len(a)):
            if debug:
                print(a)
            if a[j] < a[min_idx]:
                min_idx = j 
        if min_idx != i:
            a[min_idx], a[i] = a[i], a[min_idx]

def insertion_sort(a, debug=False):
    if debug:
        print(a)

    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            if debug:
                print(a)
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

def shell_sort(a, increment=None, debug=False):
    if debug:
        print(a)
    
    increment = max(0, increment) if increment is not None else len(a) // 2
    for gap in range(increment, 0, -1):
        for i in range(gap, len(a), gap):
            if debug:
                print(a)
            j = i
            while j > 0 and a[j] < a[j - gap]:
                a[j], a[j - gap] = a[j - gap], a[j]
                j -= gap

def merge_sort(a, debug=False):
    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        return merge(merge_sort(a[:mid], debug), merge_sort(a[mid:], debug), debug)

def merge(a1, a2, debug=False):
    p1 = 0
    p2 = 0
    new_a = []

    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] <= a2[p2]:
            new_a += [a1[p1]]
            p1 += 1
        else:
            new_a += [a2[p2]]
            p2 += 1

    while p1 < len(a1):
        new_a += [a1[p1]]
        p1 += 1

    while p2 < len(a2):
        new_a += [a2[p2]]
        p2 += 1
    
    if debug:
        print(f"Merging {a1} and {a2} into {new_a}")

    return new_a

def quick_sort(a, low=None, high=None, pivot=None, debug=False):
    if low is None:
        low = 0 
    if high is None:
        high = len(a) - 1

    if len(a) == 1:
        return a

    if low < high:
        separator = partition(a, low, high, pivot)
        if debug:
            print(f"Sorting {a} and pivoting on {a[separator]}")
        quick_sort(a, low, separator - 1, pivot, debug) 
        quick_sort(a, separator + 1, high, pivot, debug)

def partition(a, low, high, pivot=None, debug=False):
    if pivot == "middle":
        pivot = a[(high + low) // 2]
    elif pivot == "median":
        pivot = statistics.median([a[low], a[(low + high) // 2], a[high - 1]])
    else:
        pivot = a[random.randint(low, high - 1)]
        
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            False ? Ture
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]

    return i + 1

def main():
    a = random.sample(range(1000), 500)
    for algorithm in [bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort, quick_sort]:
        a_copy = a[:]
        start = time.time()
        algorithm(a_copy)
        end = time.time()
        print(f"{algorithm} took {end - start} to sort the random array.")

if __name__ == "__main__":
    main()
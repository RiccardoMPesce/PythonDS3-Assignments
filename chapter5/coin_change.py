import math


def subset_finder(subset, tot):
    sums = [0] + [math.inf] * tot
    used_elements = [[] for _ in range(tot + 1)]

    for i in range(1, tot + 1):
        min_sum = math.inf
        used = []
        for j in [c for c in subset if c <= i]:
            if 1 + sums[i - j] < min_sum:
                min_sum = 1 + sums[i - j]
                used = [j] + used_elements[i - j]
        sums[i] = min_sum
        used_elements[i] = used

    result = sums[tot] if sums[tot] is not math.inf else 0

    return result, used_elements[tot]


def main():
    print(subset_finder([1, 2, 3], 63))


if __name__ == "__main__":
    main()

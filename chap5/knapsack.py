
def find_best_combination(v, w, max_weight):
    """
    Given the maximum weight that can be held,
    find the best combbination of items which 
    maximizes the total value.
    Input: 
    - items dict, where keys are "id", "w" (weight) and "v" (value)
    - max_weight, the maximum weight of items which 
    can be held
    Output: 
    - dictionary where keys are the ids of the items, and value the amount of them. These will 
    maximize our value
    """
    value_tab = [[0 for _ in range(max_weight + 1)] for _ in range(len(v) + 1)]
    combinations = [[[] for _ in range(max_weight + 1)]
                    for _ in range(len(v) + 1)]

    for i in range(1, len(v) + 1):
        for j in range(1, max_weight + 1):
            value_tab[i][j] = value_tab[i - 1][j]
            combinations[i][j] = combinations[i - 1][j]
            if j - w[i - 1] >= 0:
                if v[i - 1] + value_tab[i - 1][j - w[i - 1]] > value_tab[i][j]:
                    value_tab[i][j] = v[i - 1] + value_tab[i - 1][j - w[i - 1]]
                    combinations[i][j] = combinations[i -
                                                      1][j - w[i - 1]] + [i]

    return value_tab[len(v)][max_weight], combinations[len(v)][max_weight]


def main():
    v = [3, 4, 8, 8, 10]
    w = [2, 3, 4, 5, 9]

    print(find_best_combination(v, w, 10))


if __name__ == "__main__":
    main()

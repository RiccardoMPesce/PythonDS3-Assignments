def min_edit_distance(original, modified):
    t1 = list(original.lower())
    t2 = list(modified.lower())

    return -1


def main():
    print(min_edit_distance("alligator", "algorithm"))


if __name__ == "__main__":
    main()

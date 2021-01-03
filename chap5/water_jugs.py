def pour_to_other_jug(q1, q2, c1, c2, q, visited):
    if q1 == q or q2 == q:
        print("Found " + str((q1, q2)))
        return True
    elif (q1, q2) in visited:
        return False
    else:
        print("Visiting " + str((q1, q2)))
        visited[(q1, q2)] = True
        left_in_q1 = c1 - q1
        left_in_q2 = c2 - q2

        to_q1 = left_in_q1 if q2 >= left_in_q1 else q2
        new_q2 = q2 - to_q1

        to_q2 = left_in_q2 if q1 >= left_in_q1 else q1
        new_q1 = q1 - to_q2

        return (
            pour_to_other_jug(c1, c2, c1, c2, q, visited) or
            pour_to_other_jug(c1, 0, c1, c2, q, visited) or
            pour_to_other_jug(0, c2, c1, c2, q, visited) or
            pour_to_other_jug(q1 + to_q1, new_q2, c1, c2, q, visited) or
            pour_to_other_jug(new_q1, q2 + to_q2, c1, c2, q, visited)
        )


def main():
    print(pour_to_other_jug(0, 0, 4, 3, 2, {}))


if __name__ == "__main__":
    main()

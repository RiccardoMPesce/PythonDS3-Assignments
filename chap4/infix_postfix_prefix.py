def is_operator(ch):
    return ch in ["+", "-", "*", "/", "**", "^"]


def is_operand(ch):
    return ch.isalpha() or ch.isdigit()


def priority(ch):
    return {
        "(": 0,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "**": 3,
        "^": 3
    }.get(ch, -1)


def infix_to_postfix(expr):
    pass


def infix_to_prefix(expr):
    pass


def main():
    pass


if __name__ == "__main__":
    main()

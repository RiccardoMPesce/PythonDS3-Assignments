def decimal_to_base(n: int, base: int) -> str:
    rems = []
    digits = "0123456789ABCDEF"
    conv = ""

    while n > 0:
        rem = n % base
        rems.append(rem)
        n //= base

    while not rems.is_empty():
        conv += digits[rems.pop()]

    return conv

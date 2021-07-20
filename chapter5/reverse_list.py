def reverse(ls):
    if len(ls) <= 1:
        return ls
    else:
        return [ls[-1]] + reverse(ls[1:-1]) + [ls[0]]

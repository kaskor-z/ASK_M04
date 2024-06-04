from math import inf


def divide(first, second):
    if second == 0:
        return str(inf)
    else:
        return str(first / second)

def gcd(a, b):
    if a < b:
        a, b = b, a

    if a == 0 or b == 0:
        return None

    while a%b > 0:
        a, b = b, a%b

    return b


test_cases = [
    (3, 3, 3),
    (0, 1, None),
    (15, 10, 5),
    (10, 20, 10),
    (1112, 695, 139),
    (695, 1112, 139),
]


def test():
    for a, b, out in test_cases:
        got = gcd(a, b)
        if got != out:
            print(f"Fail: a: {a}; b: {b}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

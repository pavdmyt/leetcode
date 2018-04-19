def fact(x):
    return x > 1 and x * fact(x - 1) or 1


test_cases = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (8, 40320),
    (10, 3628800),
]


def test():
    for n, out in test_cases:
        got = fact(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

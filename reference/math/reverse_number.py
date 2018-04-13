def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    negative = x < 0
    if negative:
        x *= -1

    rev_num = 0
    while x > 0:
        rev_num = rev_num * 10 + x%10
        x //= 10

    if negative:
        rev_num *= -1

    return rev_num


test_cases = [
    (0, 0),
    (12, 21),
    (1, 1),
    (-2, -2),
    (-5743, -3475),
    (123, 321),
    (351, 153),
    (1534236469, 9646324351),
]


def test():
    for n, out in test_cases:
        got = reverse(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

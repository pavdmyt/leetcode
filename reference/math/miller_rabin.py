from random import randrange


def is_prime(n, k=30):
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    if n <= 3:
        return n == 2 or n == 3
    neg_one = n - 1

    # write n-1 as 2^s*d where d is odd
    s, d = 0, neg_one
    while not d & 1:
        s, d = s+1, d>>1
    assert 2 ** s * d == neg_one and d & 1

    for i in range(k):
        a = randrange(2, neg_one)
        x = pow(a, d, n)
        if x in (1, neg_one):
            continue
        for r in range(1, s):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == neg_one:
                break
        else:
            return False
    return True


test_cases = [
    (1, False),
    (33, False),
    (1729, False),
    (112314134134132, False),
    (135135134136615, False),
    (2, True),
    (3, True),
    (11, True),
    (619, True),
    (997, True),
]


def test():
    for n, out in test_cases:
        got = is_prime(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

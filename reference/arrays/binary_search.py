def iterative(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return recursive(alist[:midpoint],item)
            else:
                return recursive(alist[midpoint+1:],item)


test_cases = [
    ([], 42, False),
    ([1, 42], 42, True),
    (list(range(50, 101)), 60, True),
    (list(range(50, 101)), 40, False),
]


def test_iterative():
    for alist, item, out in test_cases:
        got = iterative(alist, item)
        if got != out:
            print(f"Fail: alist: {alist}; item: {item}; "
                  f"expected: {out}; got: {got}")


def test_recursive():
    for alist, item, out in test_cases:
        got = recursive(alist, item)
        if got != out:
            print(f"Fail: alist: {alist}; item: {item}; "
                  f"expected: {out}; got: {got}")


if __name__ == '__main__':
    test_iterative()
    test_recursive()

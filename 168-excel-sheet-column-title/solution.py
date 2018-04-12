class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n > 0:
            mod = n%26
            letter = chr(mod+64) if mod != 0 else 'Z'
            title += letter
            n = n // 26 if mod != 0 else n // 27

        return title[::-1]


test_cases = [
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (26, 'Z'),
    (27, 'AA'),
    (28, 'AB'),
    (52, 'AZ'),
    (53, 'BA'),
    (122, 'DR'),
    (135, 'EE'),
]


def test():
    for n, out in test_cases:
        got = Solution().convertToTitle(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

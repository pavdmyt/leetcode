class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        if x == self.reverse(x):
            return True
        return False


    @staticmethod
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
    (-1, False),
    (10, False),
    (123, False),
    (0, True),
    (3, True),
    (11, True),
    (323, True),
]


def test():
    for n, out in test_cases:
        got = Solution().isPalindrome(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

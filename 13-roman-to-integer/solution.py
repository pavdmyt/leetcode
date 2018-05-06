class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        i = 0
        res = 0
        while i < len(s):
            sl = s[i:i+2]
            if sl in dct:
                res += dct[sl]
                i += 2
            else:
                res += dct[sl[0]]
                i += 1
        return res


test_cases = [
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (12, "XII"),
    (42, "XLII"),
    (58, "LVIII"),
    (255, "CCLV"),
    (1994, "MCMXCIV"),
]


def test():
    for out, s in test_cases:
        got = Solution().romanToInt(s)
        if got != out:
            print(f"Fail: s: {s}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

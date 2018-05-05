from collections import OrderedDict


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dct = OrderedDict()
        dct[1] = "I"
        dct[4] = "IV"
        dct[5] = "V"
        dct[9] = "IX"
        dct[10] = "X"
        dct[40] = "XL"
        dct[50] = "L"
        dct[90] = "XC"
        dct[100] = "C"
        dct[400] = "CD"
        dct[500] = "D"
        dct[900] = "CM"
        dct[1000] = "M"

        keys = list(dct.keys())
        max_num = keys[-1]
        roman = ""

        while num > 0:
            for i, key in enumerate(keys):

                if num >= max_num:
                    roman += dct[max_num]
                    num -= max_num
                    break

                if key == num:
                    roman += dct[key]
                    num -= key
                    break

                if key > num:
                    prev = keys[i-1]
                    roman += dct[prev]
                    num -= prev
                    break

        return roman


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
    for n, out in test_cases:
        got = Solution().intToRoman(n)
        if got != out:
            print(f"Fail: n: {n}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

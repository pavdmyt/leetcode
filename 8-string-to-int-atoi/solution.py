class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        is_num = lambda ch: 48 <= ord(ch) <= 57
        is_wh = lambda ch: ch == " "
        is_sign = lambda ch: ch == "-" or ch == "+"
        is_junk = lambda ch: not (is_num(ch) or is_wh(ch) or is_sign(ch))

        res = ""
        num_seen = False

        for i, ch in enumerate(s):

            if is_junk(ch):
                break

            if is_wh(ch):
                if num_seen:
                    break
                continue

            if is_num(ch):
                num_seen = True
                res += ch

            if is_sign(ch):
                if num_seen:
                    break
                else:
                    if i < len(s)-1:
                        nxt = s[i+1]
                        if is_num(nxt):
                            res += ch
                        else:
                            break

        num = int(res) if res else 0
        # int32 handling
        return max(min(num, 2**31 - 1), -2**31)


test_cases = [
    ("42", 42),
    ("   -42", -42),
    ("-   234", 0),
    ("   +0 123", 0),
    ("+1", 1),
    ("-5-", -5),
    ("+-2", 0),
    ("-", 0),
    ("0-1", 0),
    ("3.141592", 3),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    (str(2**35), 2**31-1),
]


def test():
    for s, out in test_cases:
        got = Solution().myAtoi(s)
        if got != out:
            print(f"Fail: s: {s}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

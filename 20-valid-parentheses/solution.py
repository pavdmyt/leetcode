class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in m.values():
                stack.append(ch)
            elif ch in m.keys():
                if not stack or m[ch] != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0


test_cases = [
    ("(){}[]", True),
    ("(([]{}))()", True),
    ("([)]", False),
]

def test():
    for s, out in test_cases:
        got = Solution().isValid(s)
        if got != out:
            print(f"Fail: s: {s}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

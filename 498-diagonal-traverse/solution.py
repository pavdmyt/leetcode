from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        diag_map = defaultdict(list)
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                diag_map[r+c].append(col)

        res = []
        for k, diag in diag_map.items():
            if k % 2 == 0:
                res.extend(diag[::-1])
            else:
                res.extend(diag)

        return res



test_cases = [
    (
    [[0, 1],
     [2, 3]],
     [0, 1, 2, 3]
    ),
    (
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
     [1, 2, 4, 7, 5, 3, 6, 8, 9]
    ),
    (
    [[1, 2, 3, 4],
     [5, 1, 2, 3],
     [9, 5, 1, 2]],
     [1, 2, 5, 9, 1, 3, 4, 2, 5, 1, 3, 2]
    ),
]


def test():
    for mtx, out in test_cases:
        got = Solution().findDiagonalOrder(mtx)
        if got != out:
            print(f"Fail: matrix: {mtx}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

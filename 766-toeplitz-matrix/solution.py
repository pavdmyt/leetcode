class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # return all(
        #     r == 0 or c == 0 or matrix[r-1][c-1] == val
        #     for r, row in enumerate(matrix)
        #     for c, val in enumerate(row)
        # )
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True


test_cases = [
    (
    [[0, 1],
     [0, 0]],
     True
    ),
    (
    [[1,2,3,4],
     [5,1,2,3],
     [9,5,1,2]],
     True
    ),
    (
    [[1, 2],
     [1, 2]],
     False
    ),
]


def test():
    for mtx, out in test_cases:
        got = Solution().isToeplitzMatrix(mtx)
        if got != out:
            print(f"Fail: matrix: {mtx}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

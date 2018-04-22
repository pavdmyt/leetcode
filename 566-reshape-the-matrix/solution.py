class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])
        if r * c != rows * cols:
            return nums

        mtx = []
        flat_mtx = [item for row in nums for item in row]
        i = 0
        for _ in range(r):
            mtx.append(flat_mtx[i:i+c])
            i += c

        return mtx


test_cases = [
    (
    [[1, 2],
     [3, 4]],
     1, 4,
     [[1, 2, 3, 4]]
    ),
    (
    [[1, 2],
     [3, 4]],
     2, 4,
     [[1, 2], [3, 4]]
    ),
]


def test():
    for mtx, r, c, out in test_cases:
        got = Solution().matrixReshape(mtx, r, c)
        if got != out:
            print(f"Fail: matrix: {mtx}; expected: {out}; got: {got}")


if __name__ == '__main__':
    test()

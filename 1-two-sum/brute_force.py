class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, i_val in enumerate(nums[:-1]):
            for j, j_val in enumerate(nums[i+1:]):
                if i_val + j_val == target:
                    return [i, j+i+1]
        raise RuntimeError(
            "twoSum: no solution for {0} and target {1}".format(nums, target)
        )

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ind, found = self.bin_search(nums, target)
        if found:
            return ind

        for i, num in enumerate(nums):
            if num > target:
                return i

        return len(nums)


    @staticmethod
    def bin_search(lst, target):
        first = 0
        last = len(lst) - 1
        midpoint = 0
        found = False

        while first <= last and not found:
            midpoint = (first + last) // 2

            if lst[midpoint] == target:
                found = True
            else:
                if target < lst[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return midpoint, found

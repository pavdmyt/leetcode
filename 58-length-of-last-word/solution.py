class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        split = s.split()
        if split:
            return len(split[-1])
        return 0

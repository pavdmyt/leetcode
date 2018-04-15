class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_sqaures = lambda n: sum([int(i)**2 for i in str(n)])
        return n == 1 or n > 4 and self.isHappy(sum_sqaures(n))

    # def isHappy(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     s = set()
    #     while n not in s:
    #         s.add(n)
    #         n = sum([int(i)**2 for i in str(n)])
    #     return n == 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def read_num(node):
            num = ""
            curr = node
            while curr:
                num += str(curr.val)
                curr = curr.next
            return int(num[::-1])

        num1 = read_num(l1)
        num2 = read_num(l2)
        res = num1 + num2

        tail = None
        for d in str(res):
            node = ListNode(int(d))
            node.next = tail
            tail = node

        return tail

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = ListNode(-1)
        prev.next = head
        curr = prev

        while curr:
            nxt = curr.next
            if nxt and nxt.val == val:
                curr.next = nxt.next
            else:
                curr = nxt

        return prev.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

    # def deleteDuplicates(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     prev = ListNode(None)
    #     prev.next = head
    #     curr = prev
    #
    #     while curr:
    #         nxt = curr.next
    #         while nxt and curr.val == nxt.val:
    #             nxt = nxt.next
    #
    #         curr.next = nxt
    #         curr = nxt
    #
    #     return prev.next

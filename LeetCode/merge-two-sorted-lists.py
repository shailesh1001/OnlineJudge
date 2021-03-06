# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        l = dummy
        while l1 and l2:
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l = l.next
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next
        while l1:
            l.next = ListNode(l1.val)
            l = l.next
            l1 = l1.next
        while l2:
            l.next = ListNode(l2.val)
            l = l.next
            l2 = l2.next
        return dummy.next

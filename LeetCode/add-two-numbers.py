# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = l1.val + l2.val
        carry = s / 10
        l3 = ListNode(s % 10)
        temp = l3
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next
            s = l1.val + l2.val + carry
            temp.next = ListNode(s % 10)
            carry = s / 10
            temp = temp.next
        while l1.next != None:
            l1 = l1.next
            s = l1.val + carry
            temp.next = ListNode(s % 10)
            carry = s / 10
            temp = temp.next
        while l2.next !=None:
            l2 = l2.next
            s = l2.val + carry
            temp.next = ListNode(s % 10)
            carry = s / 10
            temp = temp.next
        if carry != 0:
            temp.next = ListNode(carry)
        return l3

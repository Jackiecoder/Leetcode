# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 and l2:
            ssum = l1.val + l2.val + carry
            cur.next = ListNode(ssum % 10)
            carry = ssum // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        remain = None
        if l1:
            remain = l1
        if l2:
            remain = l2
        while remain:
            ssum = remain.val + carry
            cur.next = ListNode(ssum % 10)
            carry = ssum // 10
            remain = remain.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next

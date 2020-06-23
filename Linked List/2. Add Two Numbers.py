# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummynode = ListNode(0)
        cur = dummynode
        while l1 and l2:
            sumup = l1.val + l2.val + carry
            number = sumup % 10
            carry = sumup // 10
            cur.next = ListNode(number)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
            sumup = l1.val + carry
            number = sumup % 10
            carry = sumup // 10
            cur.next = ListNode(number)
            l1 = l1.next
            cur = cur.next
        while l2:
            sumup = l2.val + carry
            number = sumup % 10
            carry = sumup // 10
            cur.next = ListNode(number)
            l2 = l2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return dummynode.next

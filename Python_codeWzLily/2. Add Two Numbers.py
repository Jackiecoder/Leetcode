# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # go through those two linked list at the same time
        # once one linked list reach the end, end the iteration and add the rest into our list
        # time O(max(n, m)), space O(max(n, m))
        # n, m are length of l1, length of l2
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tmp = val1 + val2 + carry
            carry = tmp // 10
            cur.next = ListNode(tmp % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return dummy.next

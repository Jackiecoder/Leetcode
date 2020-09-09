# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        p1 = headA
        p2 = headB
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return p1
            if not p1:
                p1 = headB
            if not p2:
                p2 = headA
        return p1

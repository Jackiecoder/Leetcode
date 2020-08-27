# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # prev -> the last node without duplication
        # cur -> cur node try to find if next node is duplicated
        # e.g.
        # 0 1 2 3 3 4 4 5
        # p         c
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            tmp = cur
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur != tmp:
                cur = cur.next
                prev.next = cur
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        return dummy.next

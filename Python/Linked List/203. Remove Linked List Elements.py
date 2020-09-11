# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Time O(n), space O(1)
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next

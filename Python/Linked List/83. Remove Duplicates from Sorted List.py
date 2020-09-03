# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

    def deleteDuplicates_wz_dummy(self, head: ListNode) -> ListNode:
        visited = set()
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        cur = head
        while cur:
            if cur.val in visited:
                prev.next = cur.next
                cur = cur.next
            else:
                visited.add(cur.val)
                prev = cur
                cur = cur.next
        return dummy.next

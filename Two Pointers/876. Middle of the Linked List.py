# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 1 -> 1
        # 2 -> 2
        # 3 -> 2
        # 4 -> 3
        # 5 -> 3
        # ...
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while True:
            slow = slow.next
            if not fast.next or not fast.next.next:
                break
            fast = fast.next.next
        return slow

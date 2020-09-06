# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # slow fast pointer
        # start from head
        # slow move 1 step forward
        # fast move 2 step2 forward
        # e.g.
        #   [1,2,3,4,5]
        #   slow = 1 -> 2          -> 3
        #   fast = 2 -> 4 -> break
        # e.g.
        #   [1,2,3,4,5,6]
        #   slow = 1 -> 2 -> 3          -> 4
        #   fast = 2 -> 4 -> 6 -> break
        # Time O(n), space O(1)
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next

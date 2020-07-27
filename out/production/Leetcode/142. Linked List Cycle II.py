# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #                       x
        #                    x     x2
        #     x  x  x  x  x1         x
        #                    x     x
        #                       x
        # let's assume the beginning of loop is x1
        # fast move: x1 + x2 + x3 + x2
        # slow move: x1 + x2
        # so x1 + x2 = x3 + x2
        # -> x1 = x3
        # time O(n), space O(1)
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        is_cycle = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
        if not is_cycle:
            return None
        new_slow = dummy
        while new_slow != slow:
            slow = slow.next
            new_slow = new_slow.next
        return slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        reverse_times = n - m + 1
        while m > 1:
            prev = prev.next
            m -= 1
        left = prev
        prev, tail = None, prev.next
        cur = tail
        while reverse_times > 0:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            reverse_times -= 1
        left.next = prev
        tail.next = next_node
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # divide and conquer
        # 1. find middle and divide
        # 2. sort each half
        # 3. merge together
        # Time O(nlogn), space O(1)

        # how to find the middle
        # 1. slow = fast = head, while fast and fast.next
        #    when loop ends, slow is the head of second half

        # 2. slow = head, fast = head.next, while fast and fast.next
        #    when loop ends, first half >= second half
        #
        return self.divide(head)

    def divide(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        left = self.divide(head)
        right = self.divide(second)
        return self.merge(left, right)

    def merge(self, head1, head2):
        m, n = head1, head2
        dummy = ListNode(0)
        cur = dummy
        while m and n:
            if m.val <= n.val:
                cur.next = m
                m = m.next
            else:
                cur.next = n
                n = n.next
            cur = cur.next
        if m:
            cur.next = m
        if n:
            cur.next = n
        return dummy.next

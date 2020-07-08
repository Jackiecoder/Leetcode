# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # divide and conquer
        # there will be logk levels, and in each level we need to merge n times
        # time O(nlogk), space O(1)
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, l, r):
        dummy = ListNode(0)
        cur = dummy
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
                cur = cur.next
            else:
                cur.next = r
                r = r.next
                cur = cur.next
        cur.next = l or r
        return dummy.next

    def mergeKLists_heap(self, lists: List[ListNode]) -> ListNode:
        # heap
        # dummy -> node(1) -> node(1) -> node(2) -> node(3) -> node(4) -> node(4) -> node(5) -> node(6)
        # k sorted list and there are n node
        # heapify O(k)
        # heappop + heappush O(logk) * n
        # Time O(nlogk), space O(k + n)
        if not lists or all([not ls for ls in lists]):
            return None
        if len(lists) == 1:
            return lists[0]
        dummy = ListNode(0)
        cur = dummy
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        while heap:
            _, index, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        return dummy.next

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # when reach node 3 -> go child first, then go next
        # thus i need to store node3.next
        # store 3.next, store 8.next
        # thus LIFO -> stack
        # e.g.
        #
        # time O(n), space O(n)

        # stack = [4]
        # 1->2->3->7->8->11->12->

        if not head:
            return head
        dummy = Node(0, None, None, None)
        cur = dummy
        stack = [head]
        while stack:
            next_node = stack.pop()
            cur.next = next_node
            cur.child = None
            next_node.prev = cur
            cur = cur.next
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
        dummy.next.prev = None
        return dummy.next

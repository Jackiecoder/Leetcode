"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # one pass
        # 1. use defaultdict to store {original node: new node}
        # 2. once random/next point to a node which is not created yet, we just create a default node, and change its value later.
        # Time O(n), space O(n)
        if not head:
            return
        dic = defaultdict(lambda: Node(0))
        cur = head
        while cur:
            dic[cur].val = cur.val
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]

    def copyRandomList_twopass(self, head: 'Node') -> 'Node':
        # two pass
        # 1. create each node first, and store them into hashmap
        # 2. go through the linked list, and make pointer
        # Time O(2n), space O(n)
        if not head:
            return
        dic = {}
        m = n = head
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            if n.next:
                dic[n].next = dic[n.next]
            if n.random:
                dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

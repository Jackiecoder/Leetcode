"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, head: 'Node') -> 'Node':
        # queue = []
        # prev_to_new = {head: new_head}
        if not head:
            return
        queue = collections.deque([head])
        prev_to_new = {head: Node(head.val, [])}
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in prev_to_new:
                    prev_to_new[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                prev_to_new[node].neighbors.append(prev_to_new[neighbor])
        return prev_to_new[head]

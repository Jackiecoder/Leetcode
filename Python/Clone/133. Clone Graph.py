"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # use hash map to store {original node: new clone node}
        # then use BFS/DFS to go through the whole table.
        # Time O(n), space O(n)
        if not node:
            return
        head = node
        ori_to_clone = defaultdict(lambda: Node())
        queue = deque([node])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            ori_to_clone[node].val = node.val
            for neighbor in node.neighbors:
                ori_to_clone[node].neighbors.append(ori_to_clone[neighbor])
                queue.append(neighbor)
        return ori_to_clone[head]

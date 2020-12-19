"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs to go through whole graph, and use hash map to store prev -> clone node
        # Time O(n), space O(n)

        if not node:
            return None
        queue = deque([node])
        old_new = {node: Node(node.val)}
        visited = set()
        while queue:
            old_node = queue.popleft()
            if old_node in visited:
                continue
            visited.add(old_node)
            new_node = old_new[old_node]
            for neighbor in old_node.neighbors:
                queue.append(neighbor)
                if neighbor in old_new:
                    new_neighbor = old_new[neighbor]
                else:
                    new_neighbor = Node(neighbor.val)
                    old_new[neighbor] = new_neighbor
                new_node.neighbors.append(new_neighbor)
        return old_new[node]

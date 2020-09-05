"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # Follow up
        # The difference is that circuit might exist in this tree
        if not root:
            return
        dic = defaultdict(lambda: Node())
        queue = deque([root])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            dic[node].val = node.val
            for child in node.children:
                dic[node].children.append(dic[child])
                queue.append(child)
        return dic[root]

    def cloneTree_original(self, root: 'Node') -> 'Node':
        # BFS
        # Time O(n), space O(n)
        if not root:
            return
        dic = defaultdict(lambda: Node())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            dic[node].val = node.val
            for child in node.children:
                dic[node].children.append(dic[child])
                queue.append(child)
        return dic[root]

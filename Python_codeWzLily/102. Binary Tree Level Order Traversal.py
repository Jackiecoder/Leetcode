# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        # use a queue to store current level nodes
        # Time O(n), space O(n)
        if not root:
            return []
        queue = deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res

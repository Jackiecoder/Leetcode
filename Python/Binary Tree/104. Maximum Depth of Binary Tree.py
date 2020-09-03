# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # BFS
        # queue = [(node, level)]
        # time O(n), space O(n)
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        max_lvl = 0
        while queue:
            node, lvl = queue.popleft()
            max_lvl = max(max_lvl, lvl)
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        return max_lvl

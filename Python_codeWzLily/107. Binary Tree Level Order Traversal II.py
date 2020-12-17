# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # method2:
        # DFS and reverse
        # in dfs process, the root go left node first and then the right node, thus the left node will always be reached firstly
        res = []
        self.dfs(root, 0, res)
        return res[::-1]

    def dfs(self, root, lvl, res):
        if not root:
            return
        if lvl >= len(res):
            res.append([])
        res[lvl].append(root.val)
        self.dfs(root.left, lvl + 1, res)
        self.dfs(root.right, lvl + 1, res)

    def levelOrderBottom_bfs(self, root: TreeNode) -> List[List[int]]:
        # method1:
        # BFS level by level and reverse it
        if not root:
            return
        queue = deque([(root, 0)])
        res = []
        while queue:
            node, lvl = queue.popleft()
            if lvl >= len(res):
                res.append([])
            res[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        return res[::-1]

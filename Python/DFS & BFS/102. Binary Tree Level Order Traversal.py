# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS, store level
        # Time O(n), space O(n)
        if not root:
            return []
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, lvl = queue.popleft()
            if lvl >= len(res):
                res.append([])
            res[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        return res

    def levelOrder_bfs_for(self, root: TreeNode) -> List[List[int]]:
        # BFS, for loop
        # Time O(n), Space O(n)
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

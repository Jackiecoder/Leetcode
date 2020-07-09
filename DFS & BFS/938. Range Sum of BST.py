# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # if node.val in range:
        #   left and right
        # if node.val < L:
        #   go node.right
        # if node.val > R:
        #   go node.left
        #       10
        #    5      15
        #  3   7   x  18
        # L, R = 7, 15
        # BFS -> SEARCH
        # queue = []
        # sum = 10 + 15 + 7
        # Time O(n), space O(n)
        #      10
        #   5.     15
        # . 3. 7   13  18
        # 1.     6
        # res =  10 +
        # queue = 5,
        if not root:
            return 0
        queue = deque([root])
        res = 0
        while queue:
            # node in queue have possiblity to be invalid
            node = queue.popleft()
            if not node:
                continue
            if L <= node.val <= R:
                res += node.val
                queue.append(node.left)
                queue.append(node.right)
            elif node.val < L:
                queue.append(node.right)
            else:
                queue.append(node.left)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # same as lc 102
        # just add a flag to show the order of this level
        if not root:
            return []
        queue = deque([root])
        sort = True
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sort:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            sort = not sort
        return res

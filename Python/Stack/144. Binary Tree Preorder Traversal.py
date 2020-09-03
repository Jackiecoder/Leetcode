# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative -> use 'stack' to simulate system stack
        # push right, then push left
        stack = collections.deque([root])
        path = []
        while stack:
            node = stack.pop()
            if node:
                path.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return path

        '''
        # recursion -> node.val then node.left then node.right
        # time O(n), space O(n)
        
        res = []
        self.preorderTraversal_subtree(root, res)
        return res
        
    def preorderTraversal_subtree(self, node, res):
        if node:
            res.append(node.val)
            self.preorderTraversal_subtree(node.left, res)
            self.preorderTraversal_subtree(node.right, res)
        '''

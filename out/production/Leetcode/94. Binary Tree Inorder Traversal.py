# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        res = []
        stack = collections.deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp_node = stack.pop()
                res.append(tmp_node.val)
                root = tmp_node.right
        return res


'''       
# recursive
#         inorder = []
#         self.inorderTraversal_subtree(root, inorder)
#         return inorder
        
#     def inorderTraversal_subtree(self, node, res):
#         if not node:
#             return
#         self.inorderTraversal_subtree(node.left, res)
#         res.append(node.val)
#         self.inorderTraversal_subtree(node.right, res)
            '''

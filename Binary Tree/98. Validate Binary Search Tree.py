# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # according the description, the BST is a unique BST which means there will not have any duplicated value in the tree.
        # thus the left and right subtree must be BST
        # Time O(n), space O(1)
        return self.validBST(root)[0]

    def validBST(self, root):
        # return isvalid, min, max
        if not root:
            return True, float('inf'), -float('inf')
        l_valid, l_min, l_max = self.validBST(root.left)
        r_valid, r_min, r_max = self.validBST(root.right)
        # for the range
        #   l_max < root.val < r_min
        #   r_max = max(r_max, root.val)
        #   l_min = min(l_min, root.val)
        if not l_valid or not r_valid or not l_max < root.val < r_min:
            return False, None, None
        return True, min(l_min, root.val), max(r_max, root.val)

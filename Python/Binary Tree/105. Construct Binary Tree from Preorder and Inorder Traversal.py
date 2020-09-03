# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder = [(root), (left), (right)]
        # inorder  = [(left), (root), (right)]
        # choose root as root
        #   find root in inorder array
        # time O(n), space O(n)
        inorder_index = {node_val: index for index,
                         node_val in enumerate(inorder)}
        return self.buildSubtree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inorder_index)

    def buildSubtree(self, preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_index):
        if pre_start > pre_end or in_start > in_end:
            return None
        # when function run here, root must be valid
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        root_in_inorder = inorder_index[root_val]
        left_length, right_length = root_in_inorder - in_start, in_end - root_in_inorder
        root.left = self.buildSubtree(preorder, pre_start + 1, pre_start + left_length,
                                      inorder, in_start, in_start + left_length - 1, inorder_index)
        root.right = self.buildSubtree(preorder, pre_start + left_length + 1,
                                       pre_end, inorder, in_start + left_length + 1, in_end, inorder_index)
        return root

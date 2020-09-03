# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # we can use a hash table to store the index of each node.val
        # in this case, we only need O(logn + n) time to solve it
        val_to_index = {val: i for i, val in enumerate(inorder)}
        return self.buildSubtree(preorder, 0, len(preorder), inorder, 0, len(inorder), val_to_index)

    def buildSubtree(self, preorder, pre_l, pre_r, inorder, in_l, in_r, val_to_index):
        # print(preorder[pre_l: pre_r + 1], (pre_l, pre_r), inorder[in_l: in_r  +1], (in_l, in_r))
        if pre_l >= pre_r or in_l >= in_r:
            return
        root_val = preorder[pre_l]
        # pre_l + 1 : index + 1,   index + 1 : pre_r
        # in_l : index,     index + 1 : in_r
        root = TreeNode(root_val)
        index = val_to_index[root_val]
        left_length = index - in_l
        # right_length = in_r - index - 1
        root.left = self.buildSubtree(
            preorder, pre_l + 1, pre_l + left_length + 1, inorder, in_l, index, val_to_index)
        root.right = self.buildSubtree(
            preorder, pre_l + left_length + 1, pre_r, inorder, index + 1, in_r, val_to_index)
        return root

    def buildTree_recursive(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder = [root, (left), (right)]
        # inorder  = [(left), root, (right)]
        # preorder[0] -> root
        # find root at inorder[index]
        # root.left -> buildTree(inorder[:index])
        # root.right ->buildTree(inorder[index + 1:])
        # time O(nlogn), space O(1)
        if preorder:
            root_val = preorder[0]
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            root.left = self.buildTree(
                preorder[1: index + 1], inorder[0: index])
            root.right = self.buildTree(
                preorder[index + 1:], inorder[index + 1:])
            return root

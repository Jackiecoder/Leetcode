# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        # 1. BST, for each node, traverse another BST,
        #   time O(nlogn), space O(1)
        # 2. hash set,
        #   traverse the first tree, and save all remains
        #   traverse the second tree, and find if the remain is in the tree
        #  time O(n), space O(n)
        # 3. stack
        #   stack 1 store the left nodes
        #   stack 2 store the right nodes
        #   time O(n + m), space O(h1 + h2)

        stack1, stack2 = [], []
        while root1:
            stack1.append(root1)
            root1 = root1.left
        while root2:
            stack2.append(root2)
            root2 = root2.right
        while stack1 and stack2:
            summ = stack1[-1].val + stack2[-1].val
            if summ == target:
                return True
            elif summ < target:
                root1 = stack1.pop().right
                while root1:
                    stack1.append(root1)
                    root1 = root1.left
            else:
                root2 = stack2.pop().left
                while root2:
                    stack2.append(root2)
                    root2 = root2.right
        return False

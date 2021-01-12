# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # brute force
        #   traverse the whole tree, and store each node
        #   then pop out the top K nodes
        # Time O(n + nlogk), space O(n)

        # traverse + binary search + two pointer
        # Time: O(n)  + O(logn) + O(k)
        # space O(n)

        inorder = []
        self.dfs(root, inorder)
        inorder = [(abs(i - target), i) for i in inorder]
        heapq.heapify(inorder)
        res = []
        while k > 0:
            diff, val = heapq.heappop(inorder)
            res.append(val)
            k -= 1
        return res

    def dfs(self, node, inorder):
        # left, root, right
        if not node:
            return
        self.dfs(node.left, inorder)
        inorder.append(node.val)
        self.dfs(node.right, inorder)

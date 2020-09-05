# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        # Time O(n), space O(n)
        if not root:
            return
        ori_to_new = defaultdict(lambda: NodeCopy())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            ori_to_new[node].val = node.val
            if node.left:
                ori_to_new[node].left = ori_to_new[node.left]
                queue.append(node.left)
            if node.right:
                ori_to_new[node].right = ori_to_new[node.right]
                queue.append(node.right)
            if node.random:
                ori_to_new[node].random = ori_to_new[node.random]
        return ori_to_new[root]

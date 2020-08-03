# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # use a hash table to store {value: [node.val]}
        # then sort hash keys
        # and make a list
        # Time O(n + klogk), n -> nodes, k -> width
        # Space O(n)
        if not root:
            return []
        val_to_nodes = defaultdict(lambda: defaultdict(list))
        queue = deque([(root, 0, 0)])
        while queue:
            node, x, y = queue.popleft()
            val_to_nodes[x][y].append(node.val)
            if node.left:
                queue.append((node.left, x - 1, y - 1))
            if node.right:
                queue.append((node.right, x + 1, y - 1))
        res = []
        for x_coordination in sorted(val_to_nodes.keys()):
            res.append([])
            for y_coordination in sorted(val_to_nodes[x_coordination], reverse=True):
                res[-1].extend(sorted(val_to_nodes[x_coordination]
                                      [y_coordination]))
        return res

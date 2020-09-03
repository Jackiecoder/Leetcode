# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # serialize tree to preorder
        # use queue to store child
        # if not child, append null
        #
        # queue = [5, #, #]
        # cur =
        # res = [1, 2, 3, 4, 5, 6, 7, #, #, #, #, #, #, #, #]
        # time O(n), space O(n)
        if not root:
            return ''
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node == "#":
                res.append("#")
                continue
            res.append(str(node.val))
            if node.left:
                queue.append(node.left)
            else:
                queue.append('#')
            if node.right:
                queue.append(node.right)
            else:
                queue.append('#')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(ls[0])
        ls = ls[1:]
        queue = deque([root])
        # #,#
        # queue = []
        # 1  -> 2, 3
        # 2 -> x, x
        # 3 -> 4, 5
        # 4 -> x, x
        while ls or queue:
            # Nodes in queue could be invalid
            # all elements are TreeNode()
            node = queue.popleft()
            left = ls[0]
            right = ls[1]
            ls = ls[2:]
            if left != '#':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

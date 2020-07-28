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
        # if we want to serialize the tree in example -> [1,2,3,null,null,4,5]
        # except the last level, all None must be pushed into queue
        # preorder
        if not root:
            return ''
        queue = deque([root])
        res = []
        while queue:
            root = queue.popleft()
            if not root:
                res.append('#')
                continue
            res.append(str(root.val))
            queue.append(root.left)
            queue.append(root.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(nodes[0])
        index = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if nodes[index + 1] != '#':
                left_node = TreeNode(nodes[index + 1])
                node.left = left_node
                queue.append(left_node)
            if nodes[index + 2] != '#':
                right_node = TreeNode(nodes[index + 2])
                node.right = right_node
                queue.append(right_node)
            index += 2
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

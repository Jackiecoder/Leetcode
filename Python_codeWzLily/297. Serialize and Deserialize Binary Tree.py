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
        # BFS
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    res.append("null")
                    continue
                else:
                    res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            left_val, right_val = data[index], data[index + 1]
            index += 2
            if left_val != "null":
                left_node = TreeNode(left_val)
                node.left = left_node
                queue.append(left_node)
            if right_val != "null":
                right_node = TreeNode(right_val)
                node.right = right_node
                queue.append(right_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

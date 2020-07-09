# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    # idea:
    # push all left node to stack
    # e.g.
    #           7
    #       3.     15
    #     4.  6.  9.  20
    # stack = [7, 3, 4]
    #
    # Q: why the time is O(1)?
    # A: Each node has been visited twice (push and pop)
    #    and if we want to visit all nodes, we will call next() n times
    #    which makes our time complexity to amortized O(1)
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.push(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

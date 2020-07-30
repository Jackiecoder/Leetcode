"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect_dfs_recursion(self, root: 'Node') -> 'Node':
        # if there is no restrict of space complexity
        #   -> BFS
        # now there is no extra space requirement
        # Q: recursion stack will be calculated as the extra space?
        # A: it does't count

        # because it's a perfect binary tree
        # so it is easy to connect left child and right child
        # -> the difficulty will be how to connect node(5) with node(6)
        # so I want to get the rightmost child in the left subtree, and connect it to the left most child in the right subtree
        # edge case: like node(4), it should be connected with nothing
        #   prev -> record if there is a left node
        #
        # recursion function :
        #   1. input root
        #   2. if there is a prev node -> prev.next = left child
        #   3. connect left child and right child
        #   4. right child should be the prev

        # time O(n), space O(1)
        if not root:
            return
        self.dfs(root)
        return root

    def dfs(self, node):
        if node.left and node.right:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            self.dfs(node.left)
            self.dfs(node.right)

    def connect_dfs_stack(self, root: 'Node') -> 'Node':
        # dfs stack
        # time O(n), space O(n)
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                stack.append(node.right)
                stack.append(node.left)
        return root

    def connect_bfs(self, root: 'Node') -> 'Node':
        # BFS
        # time O(n), space O(n)
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                queue.append(node.left)
                queue.append(node.right)
        return root

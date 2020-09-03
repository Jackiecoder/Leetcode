# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView_bfs_queue(self, root: TreeNode) -> List[int]:
        # bfs + queue
        # when use bfs, we will push the right child to queue first, then the left child
        # and we don't need lvl variable to distinguish the level
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res

    def rightSideView_dfs_stack(self, root: TreeNode) -> List[int]:
        # this problem asks for the most right node in each level
        # res = [1, 3, 4, 6]
        # stack = []
        # cur =
        # lvl =
        #     -> if lvl >= len(res): res.append(cur.val)
        # time O(n), space O(n)
        if not root:
            return []
        stack = [(root, 0)]
        res = []
        while stack:
            # all node in stack are valid
            cur, lvl = stack.pop()
            if not cur:
                continue
            if lvl >= len(res):
                res.append(cur.val)
            stack.append((cur.left, lvl + 1))
            stack.append((cur.right, lvl + 1))
        return res

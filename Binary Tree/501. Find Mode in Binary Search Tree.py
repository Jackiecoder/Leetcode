# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    '''
    Time O(n), space O(n)
    '''

    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        freq = defaultdict(int)
        self.dfs(root, freq)
        max_freq = max(freq.values())
        return [k for k, v in freq.items() if v == max_freq]

    def dfs(self, root, freq):
        if not root:
            return
        freq[root.val] += 1
        self.dfs(root.left, freq)
        self.dfs(root.right, freq)

    '''
    # Without extra space
    def __init__(self):
        self.prev = None
        self.max_count = 0
        self.cur_count = 0
        self.res = []
        
    def findMode(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.res
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if root.val == self.prev:
            self.cur_count += 1
        else:
            self.cur_count = 0
        if self.cur_count == self.max_count:
            self.res.append(root.val)
        elif self.cur_count > self.max_count:
            self.res = [root.val]
            self.max_count = self.cur_count
        self.prev = root.val
        self.inorder(root.right)
    '''

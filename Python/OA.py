class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def findMissingValue(root: ListNode):
    self.missingRange = None


def findNodeRange(root, left, right):
    if not root.val:
        self.missingRange = [left, right]
    if not root.left and not root.right:
        return root.val
    if not root.left:
        self.findNodeRange(root.right, left, root.val)


'''
        5
    -       8 
  1   4 
 N 2 

'''

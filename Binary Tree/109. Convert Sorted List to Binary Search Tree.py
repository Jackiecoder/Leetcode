# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # find mid
        # head -> the node before mid   --> left subtree
        # mid.next -> tail.   ---> right subtree
        if not head:
            return None
        tmp = head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        #      [dummy, -10, -3, 0, 5, 9]
        # [dummy, -10, -3]    [dummy, 5, 9]
        # [dummy, -10]  []
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        root = TreeNode(mid.val)
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(mid.next)
        return root

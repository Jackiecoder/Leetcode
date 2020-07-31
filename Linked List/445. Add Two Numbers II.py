# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. Brutal Force
        #   reverse list 1 and list 2
        #   add them together
        #   Time O(N), where n is max(len(l1), len(l2))
        #   Space O(1)

        # 2. start from end to the head, and linked list can not go back
        # -> backtracking
        # use recursion
        #   1. get length of l1 and l2
        #   2. make the longer one move forward
        #   e.g. 7243 + 564
        #        4      3
        #        val = 7 + carry of (NEXT SUM)
        #        243 + 564
        #        val = 2 + 5 + carry of (NEXT SUM)
        #        val = 4 + 6 + carry of (NEXT SUM)
        #        val = 3 + 4
        #   1. make l1 always the longer one,
        #       if len(l1) < len(l2), swap
        #   2. recursion function -> return the carry and the node
        #       1. let l1 move forward (n - m) times to make the number at same digit
        #          node.val = cur.val + carry of (next sum)
        #          node.next = node(remain of next sum)
        #       2. same digits add up
        #           node.val = l1.val + l2.val + carry
        #           node.next = node(remain of next sum)
        #       3. when there is no next
        #           end the recursion
        #   Time O(N), n -> max(len(l1), len(l2))
        #   Space O(N)
        n, m = 0, 0
        cur = l1
        while cur:
            cur = cur.next
            n += 1
        cur = l2
        while cur:
            cur = cur.next
            m += 1
        if m > n:
            l1, l2, n, m = l2, l1, m, n
        carry, node = self.addDigit(l1, l2, n - m)
        if carry:
            dummy = ListNode(carry)
            dummy.next = node
            return dummy
        return node

    def addDigit(self, l1, l2, move):
        # return the carry and the cur node
        if move > 0:
            carry, next_node = self.addDigit(l1.next, l2, move - 1)
            ssum = carry + l1.val
            carry = ssum // 10
            node = ListNode(ssum % 10)
            node.next = next_node
            return carry, node

        if not l1 or not l2:
            return 0, None
        carry, next_node = self.addDigit(l1.next, l2.next, move)
        ssum = l1.val + l2.val + carry
        carry = ssum // 10
        node = ListNode(ssum % 10)
        node.next = next_node
        return carry, node

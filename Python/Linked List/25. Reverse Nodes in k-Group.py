# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur_dummy = dummy
        while head:
            count = k
            cur = head
            while cur and count > 0:
                # cur is the head of next linked list
                cur = cur.next
                count -= 1
            if count > 0:
                return dummy.next
            reversed_head, reversed_tail = self.reverseLinkedList(head, k)
            cur_dummy.next = reversed_head
            cur_dummy = reversed_tail
            cur_dummy.next = cur
            head = cur
        return dummy.next

    def reverseLinkedList(self, head, k):
        # return the new head
        # this function assume the list contains at least k nodes
        tmp = None
        tail = head
        while k > 0:
            next_node = head.next
            head.next = tmp
            tmp = head
            head = next_node
            k -= 1
        return tmp, tail

    def reverseKGroup_recursion(self, head: ListNode, k: int) -> ListNode:
        # 1. make sure if the remain list have k length
        # 2. if it is not have -> return head
        #    else reverse the list
        #    2.1 how to reverse k nodes?
        #       1. record head, and head.next = tail.next
        #       2. make a k times loop
        #       3. return tail
        # Time O(n), space O(1)

        cur = head
        count = k
        while cur and count > 0:
            cur = cur.next
            count -= 1
        if count > 0:
            # the length of remain part is shorter than k
            return head
        count = k - 1
        next_node = head.next
        head.next = self.reverseKGroup(cur, k)
        while count > 0:
            tmp = next_node.next
            next_node.next = head
            head = next_node
            next_node = tmp
            count -= 1
        return head

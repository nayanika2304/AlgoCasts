#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        odd = head
        even, second_node = head.next, head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            if odd.next:
                odd = odd.next
            even.next = even.next.next
            even = even.next

        # to attach the odd list to even
        odd.next = second_node
        return head




class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        newHead = None
        newTail = None
        prev = None
        current = head

        while current:
            if (prev and current.val == prev.val) or (
                    current.next and current.val == current.next.val):
                pass
            #duplicate
            else:
                if newHead == None:
                    newHead = current
                    newTail = newHead
                else:
                    newTail.next = current
                    newTail = current
            prev = current
            current = current.next
        if newTail:
            newTail.next = None
        return newHead

n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(3)
n.next.next.next.next = ListNode(4)

Solution().deleteDuplicates(n)

while n:
    print(n.val)
    n = n.next

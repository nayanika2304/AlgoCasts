class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value},{self.next})"

def rotate(node,n):
    length = 0
    curr = node
    while curr is not None:
        curr = curr.next
        length = length + 1
    n = n % length
    slow,fast = node,node
    for i in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    fast.next = node
    head = slow.next
    slow.next = None

    return head

node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(rotate(node,2))

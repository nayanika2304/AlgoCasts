class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value},{self.next})"

def remove_duplicates(node):

    curr = node

    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next

node = Node(1, Node(2, Node(2, Node(3, Node(3)))))
remove_duplicates(node)
print(node)
# (1, (2, (3, None)))

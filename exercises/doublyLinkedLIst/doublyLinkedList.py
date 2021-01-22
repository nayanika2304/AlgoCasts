class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index
        is invalid, return -1.
        """
        node = self.head
        counter = 0
        if node is None:
            return -1

        while node is not None:
            if counter == index:
                return node.data
            node = node.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked
        list. After the insertion, the new node will be the first node of the
        linked list.
        """

        newNode = Node(val)

        if self.head == None:
            self.head = self.tail = newNode

            self.head.prev = None
            self.tail.next = None

        else:
            #head's previous node will be newNode
            self.head.prev = newNode
            #newNode's next node will be head
            newNode.next = self.head
            #newNode's previous will point to None
            newNode.prev = None
            #newNode will become new head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        newNode = Node(val)
        if self.head is None:
            self.head = self.tail = newNode
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked
        list. If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the length,
        the node will not be inserted.
        """
        i = 0
        current = self.head

        while current is not None:
            if i == index:
                break
            current = current.next
            i += 1


        if i != index:
            return

        newNode = Node(val)
        newNode.prev = current
        newNode.next = current.next
        current.next = newNode
        newNode.next.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        current = self.head

        while current is not None:
            if i == index:
                break
            current = current.next
            i +=1

        if current.next == self.tail:
            return
        current.next = current.next.next
        current.next.prev = current

#Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(1)
# obj.addAtHead(2)
# obj.addAtTail(4)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# check to see if a linked list is a palindrome or not
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Palindrome:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #addNode() will add a new node to the list
    def addNode(self, data):
        #Create a new node
        newNode = Node(data)

        #Checks if the list is empty
        if(self.head == None):
            #If list is empty, both head and tail will point to new node
            self.head = newNode
            self.tail = newNode
        else:
            #newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            #newNode will become new tail of the list
            self.tail = newNode
            #Size will count the number of nodes present in the list
        self.size = self.size + 1

    def reverseLinkedList(self,temp):
        prev = None
        current = temp
        nextNode = None

        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev

    def isPalindrome(self):
        current = self.head
        flag = True

        mid = (self.size//2) if(self.size%2 == 0) else ((self.size+1)//2)

        #Finds the middle node in given singly linked list
        for i in range(1, mid):
            current = current.next

        #Reverse the list after middle node to end
        revHead = self.reverseLinkedList(current.next)

        #Compare nodes of first half and second half
        while self.head != None and revHead != None:
            if self.head.data != revHead.data:
                flag = False
                break

            self.head = self.head.next
            revHead = revHead.next

        if(flag):
            print("Given singly linked list is a palindrome")
        else:
            print("Given singly linked list is not a palindrome")

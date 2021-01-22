from collections import deque


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):

        if self.data:
            if data < self.data :
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #Left -> root -> Right
    def inorder(self,root):
        res = []
        if root :
            res = self.inorder(root.left)
            res.append(root)
            res = res + self.inorder(root.right)
        return res

    def inorderIterative(self,root):
        p = root
        stack = []
        while True:
            while p:
                stack.append(p)
                p = p.left

            if len(stack) == 0:
                break
            p = stack.pop()
            print(p.data)
            p = p.right

    # root -> left -> right
    def printPreorder(self,root):

        if root:

            # First print the data of node
            print(root.data)
            # Then recur on left child
            self.printPreorder(root.left)

            # Finally recur on right child
            self.printPreorder(root.right)

    def preorderIterative(self,root):
        p = root
        stack = []
        while True:
            while p:
                print(p.data)
                stack.append(p)
                p = p.left
            if len(stack) == 0:
                break

            p = stack.pop()
            p = p.right



    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    # Iterative function to perform post-order traversal of the tree
    def postorderIterative(self,root):

        # create an empty stack and push root node
        stack = deque()
        stack.append(root)

        # create another stack to store post-order traversal
        out = deque()

        # loop till stack is empty
        while stack:

            # we pop a node from the stack and push the data to output stack
            curr = stack.pop()
            out.append(curr.data)

            # push left and right child of popped node to the stack
            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        # print post-order traversal
        while out:
            print(out.pop(), end=' ')




root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.postorder(root)
print("---------------------")
root.postorderIterative(root)


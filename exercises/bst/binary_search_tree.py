class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def search(self,root,key):
        if root is None or root.data == key :
            return root
        if key > root.data:
            return self.search(root.right,key)

        return self.search(root.left,key)

    def binary_search(self,arr,low,high,x):
        if high < low:
            return None
        mid = (high + low)//2
        if arr[mid] > x:
            return self.binary_search(arr,low,mid -1,x)

        else:
            return self.binary_search(arr,mid + 1, high, x)
    def insert_bst(self,root,val):
        if root is None:
            return Node(val)
        else:
            if root.data == val:
                return root
            if root.data < val :
                root.right = self.insert_bst(root.right, val)
            if root.data > val :
                root.left = self.insert_bst(root.left,val)
        return root

    def inorder_successor(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_bst(self,root,val):
        if root is None:
            return root

        # if val is less than root
        if val < root.data:
            self.delete_bst(root.left,val)

        # if val is greater than root
        elif val > root.data:
            self.delete_bst(root.right,val)

        # if the key is the same as root
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children get a inorder successor(smallest value in the right subtree)
            temp = self.inorder_successor(root.right)

            # Copy the inorder successor`s content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self.delete_bst(root.right, temp.key)

        return root

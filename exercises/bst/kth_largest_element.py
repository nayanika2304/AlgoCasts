class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
        self.count = 1

class KthLargest:
    def __init__(self,k ,nums):
        self.k = k
        self.root = None
        for num in nums:
            self.root = self.insert(self.root,num)


    def insert(self,root,num):
        if root is None:
            return Node(num)
        if root.data < num:
            root.right = self.insert(root.right,num)
        else:
            root.left = self.insert(root.left,num)
        root.count += 1
        return root


    def add(self,num):
        self.root = self.insert(self.root,num)
        rest =  self.k
        current = self.root

        while current:
            right_count = current.right.count if current.right else 0
            if right_count > rest -1:
                current = current.right
            elif right_count < rest - 1:
                #print('rest',rest)
                rest = rest - right_count + 1
                current = current.left
            else:
                return current.data

k = 3
nums = [4,5,8,2]
Kthlargest = KthLargest(k,nums)
#print(Kthlargest.add(3)) #returns 4
print(Kthlargest.add(5)) #returns 5
# print(Kthlargest.add(10)) #returns 5
# print(Kthlargest.add(9)) #returns 8
# print(Kthlargest.add(4)) #returns 8

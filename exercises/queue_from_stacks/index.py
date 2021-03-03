class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,val):
        self.s1.append(val)

    def dequeue(self):
        if self.s2:
            return self.s2.pop()
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

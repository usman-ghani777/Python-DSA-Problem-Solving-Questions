class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x):
        newNode = Node(x)
        if self.front is None:   # queue empty
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def pop(self):
        if self.front is None:
            return None   # queue empty
        x = self.front.data
        self.front = self.front.next
        if self.front is None:   # queue became empty
            self.rear = None
        return x

    def getfront(self):
        if self.front is None:
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

s = Queue()
s.push(10)
s.push(20)
s.push(30)

print(s.getfront())  # 10
print(s.pop())       # 10
print(s.getfront())  # 20
print(s.size())      # 2

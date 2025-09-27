class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            return None   # or raise Exception("Stack Underflow")
        x = self.top.data
        self.top = self.top.next
        return x

    def gettop(self):
        if self.top is None:
            return None
        return self.top.data

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.gettop())  # 30
print(s.pop())     # 30
print(s.gettop())  # 20
print(s.size())    # 2

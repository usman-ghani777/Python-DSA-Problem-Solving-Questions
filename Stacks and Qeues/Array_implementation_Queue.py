class queue:
    def __init__(self):
        self.Q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.Q.append(x)

    def POP(self):
        if self.front == -1 or self.front >= len(self.Q):
            return None   # queue empty
        x = self.Q[self.front]
        self.front += 1
        if self.front == len(self.Q):  # queue empty after removal
            self.front = -1
            self.Q = []
        return x

    def getFront(self):
        if self.front == -1 or self.front >= len(self.Q):
            return None
        return self.Q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.Q) - self.front

    
Q   = queue()
Q.push(5)
Q.push(4)
Q.push(3)
Q.push(2)

print(Q.getFront())
Q.POP()
print(Q.getFront())
print(Q.size())


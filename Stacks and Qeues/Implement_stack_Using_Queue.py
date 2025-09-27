from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.Q = deque()

    def push(self, x):
        self.Q.append(x)
        # Rotate the queue to make the last pushed element the front
        for _ in range(len(self.Q) - 1):
            self.Q.append(self.Q.popleft())

    def pop(self):
        if not self.Q:
            return -1   # or raise IndexError("Stack is empty")
        return self.Q.popleft()
    
    def peek(self):
        if not self.Q:
            return -1   # or raise IndexError("Stack is empty")
        return self.Q[0]

    def size(self):
        return len(self.Q)

    def is_empty(self):
        return len(self.Q) == 0

class stack:
    def __init__(self):
        self.st = []
    
    def push(self,x):
        self.st.append(x)

   
    def POP(self):
        if len(self.st) == 0:
            return None   # safer to return None if empty
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st)==0:
            return
        return self.st[-1]
    
    def size(self):
        return len(self.st)
    

Stack = stack()
Stack.push(5)
Stack.push(4)
Stack.push(3)
Stack.push(2)

print(Stack.POP())
print(Stack.top())
print(Stack.size())


        
       

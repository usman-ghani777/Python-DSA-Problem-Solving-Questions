class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def traversal(self, head):
        if head is None:
            print("SLL is empty")
        else:
            current = head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
        print()

    def del_duplicate(self, head):
        current = head
        l = 0
        while current:
            l += 1
            current = current.next

        current = head
        for i in range(l - 1):   # stop before last node
            if current.next and current.value == current.next.value:  
                current.next = current.next.next   # remove duplicate
            else:
                current = current.next
        return head


# Create nodes
a = Node(1)
b = Node(2)
c = Node(2)
d = Node(4)

# Link nodes
a.next = b
b.next = c
c.next = d

a.del_duplicate(a)
a.traversal(a)




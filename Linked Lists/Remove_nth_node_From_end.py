class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

  
    def Delete_nth(head, n):   # make it static so it can be called with Node.Delete_nth
        current = head
        l = 0
        while current != None:
            current = current.next
            l += 1

        current = head   # reset pointer
        for i in range(l - n - 1):   # go to node before the one we delete
            current = current.next

        current.next = current.next.next
        return head
    
# Methode using Fast And Slow Pointers to delete the nth node from the end
    def delete_nth_end(self,head,n):
        p1 = head
        p2 = head

        for i in range(n):
            p2 = p2.next
        if p2==None:
            head = head.next
            return head

        while p2!=None:
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next 




    def print_list(head):
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")   # fix indentation


# Create nodes
a = Node(1)
b = Node(3)
c = Node(3)
d = Node(4)
e = Node(5)

# Link nodes
a.next = b
b.next = c
c.next = d
d.next = e

print("Original list:")
Node.print_list(a)

# Delete 2nd node from the end (which is 4)
a = Node.Delete_nth(a, 2)

print("After deleting 2nd node from end:")
Node.print_list(a)

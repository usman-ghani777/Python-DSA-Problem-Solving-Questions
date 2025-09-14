class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def delete_node(self, node):
        if node and node.next:
            node.value = node.next.value
            node.next = node.next.next

# Helper function to print list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

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
print_list(a)

# Delete node 'c' (value 3)
a.delete_node(c)

print("After deleting c (3):")
print_list(a)

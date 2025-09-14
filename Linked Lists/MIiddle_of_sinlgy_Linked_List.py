class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next   

    def MiddleNode(self, head):
        current = head
        l = 0
        while current:
            l += 1
            current = current.next

        current = head
        for _ in range(l // 2):
            current = current.next

        return current


# Create nodes
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

# Link nodes
a.next = b
b.next = c
c.next = d

# Call method correctly
mid = a.MiddleNode(a)
print("Middle node value:", mid.value)

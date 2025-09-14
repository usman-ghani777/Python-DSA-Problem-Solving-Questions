class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next  

    def delete_duplicates(self, head):
        current = head
        while current and current.next:
            if current.value == current.next.value:
            # Skip the duplicate node
                current.next = current.next.next
        else:
            # Move forward
            current = current.next
        return head

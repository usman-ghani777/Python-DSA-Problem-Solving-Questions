class node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next = next

    def print_List(head):
        if head is None:
            print("empty")
        else:
            current = head
        while current!=None:
            print(current.value,end="->")
            current = current.next
    def reverse(self,head):
        current = head
        prev = None
        nxt = None
        while current!=None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
    


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
    def rotate(self,head,k):
        if head == None or head.next == None:
            return head
        l = 0
        last = head
        while last.next!=None:
            last = last.next
            l+=1
        l+=1
        k = k%l
        
        if k==0:
            return head
        current = head

        for i in range(k-l-1):
            current = current.next

        last.next = head
        head = current.next
        current.next = None

        return head


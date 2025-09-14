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
            
    def HasCycle(self,head,k):
        fast =head
        slow = head
        while fast !=None and slow !=None:

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
            

      
      


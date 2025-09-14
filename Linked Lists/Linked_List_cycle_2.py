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
        has_cycle = False
        while fast !=None and slow !=None:

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
            if not has_cycle:
                return None
       
            l = 0
            while slow.next!= fast:
                slow = slow.next
                l+=1
            l+=1
            slow = slow.next

            for i in range(l):
                fast = fast.next
                
            while slow!=fast:
                slow = slow.next
                fast = fast.next
                 
        return slow           

      
      


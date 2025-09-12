class node:
    def __init__(self,value):
        self.value = value
        self.next  = None

class singly_Linked_List:
    def __init__(self):
        self.head = None

# Methode To append a New node
    def append(self,value):
        new_node = node(value)
        if self.head==None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
# Methode for Traversal a List
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value,end =" ")
                current = current.next
# Methode to Insert a node on a specific position
    def insert_at(self,value,position):
        new_node = node(value)
        if position ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count<position:
                prev_node = current
                current = current.next
                count+=1
            prev_node.next = new_node
            new_node.next = current
# Methode to delte the value from Linked List
    def Delete_at(self,value):
        temp = self.head
        if temp.next is not None:
            if temp.value==value:
                self.head = temp.next
                return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.value == value:
                    found = True
                    break
                prev = temp
                temp = temp.next
            if found:
                prev.next = temp.next
                return
            else:
                print("Node not Found")
                
 

# node1 = node(5)
# node2 = node(6)
# node3 = node(7)
# node4 = node(8)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# print(node1.next.value)

sll = singly_Linked_List()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traversal()





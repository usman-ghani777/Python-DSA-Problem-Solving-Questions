class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def print_list(head):
        if head is None:
            print("empty")
            return
        current = head
        while current:
            print(current.value, end="->")
            current = current.next
        print("None")

    @staticmethod
    def intersection(head1, head2):
        # Step 1: Find lengths
        l1, l2 = 0, 0
        p1, p2 = head1, head2

        while p1:
            l1 += 1
            p1 = p1.next
        while p2:
            l2 += 1
            p2 = p2.next

        # Step 2: Reset pointers
        p1, p2 = head1, head2

        # Step 3: Advance the longer list by difference
        if l1 > l2:
            for _ in range(l1 - l2):
                p1 = p1.next
        else:
            for _ in range(l2 - l1):
                p2 = p2.next

        # Step 4: Move both pointers together
        while p1 and p2:
            if p1 == p2:   # check node reference, not just value
                return p1.value
            p1 = p1.next
            p2 = p2.next

        return None
    
    
    # Another solution To Solve intersection
    def intersection2(self,head1,head2):
        count =0
        p1 = head1
        p2 = head2
        while True:
            if p1==p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if p1 ==None:
                count+=1
                p1 = head2

            if p2==None:
                p2 = head1
            if count>1:
                return None    




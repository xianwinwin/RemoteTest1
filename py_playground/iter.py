class ListNode:

    def __init__(self, val):
        self.val=val
        self.next = None

class LinkedList:

    def __init__(self, head):
        self.head = head
        self.cur = None
    
    def __iter__(self): 
        self.cur = self.head
        return self
    
    def __next__(self):

        if self.cur: 
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration

            


if __name__=='__main__':
    print ("start...")

    n1  = ListNode(1)
    n7  = ListNode(7)
    n3  = ListNode(3)
    n2  = ListNode(2)

    n1.next=n7
    n7.next=n3
    n3.next=n2

    linked_list = LinkedList(n1)

    for i in linked_list:
        print (i)

    for i in linked_list:
        print (i)

    print ("END.")
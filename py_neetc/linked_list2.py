class Node:

    def __init__(self, val):
        self.val=val
        self.next = None

class Solution:

    def reorder_list(self, root):

        #step1: get a pointer to the middle
        slow, fast = root, root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        #step2: reverse the link from the middle node to the nth
        #[7]->[3]->[8]->[12] 
        #      m    nxt
        #[7]->[3]<-[8]<-[12] 

        prv = None
        while middle:
            nxt = middle.next
            middle.next = prv
            prv = middle
            middle = nxt
        
        p1 = root
        p2 = prv
        #part 3: rehook
        
        while p1 and p2: 
            nxt = p1.next
            p1.next = p2
            tmp = p2.next
            p2.next = nxt
            p1 = nxt
            p2 = tmp  
            

        return root


if __name__=='__main__':
    print ("Start...a")

    #[1,2,7,3,8,12]
    n1 = Node(1) 
    n2 = Node(2)
    n7 = Node(7)
    n3 = Node(3)
    n8 = Node(8)
    n12 = Node(12)

    n1.next=n2
    n2.next=n7
    n7.next=n3
    n3.next=n8
    n8.next=n12

    print ("BEFORE")
    ptr = n1
    while ptr:
        print(ptr.val)
        ptr=ptr.next

    ptr = n1        

    print ("and AFTER:")  #[1,12,2,8,7,3]
    s = Solution()
    r = s.reorder_list(ptr)
    while r:
        print(r.val)
        r=r.next

    print ("END!")
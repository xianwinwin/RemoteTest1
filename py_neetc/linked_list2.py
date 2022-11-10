
class Node:

    def __init__(self, val):
        self.val=val
        self.next = None


class Solution:

    def reorder_list(self, root):

        print ("im in")
        #step1: get a pointer to the middle
        slow, fast = root, root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        #step2: reverse the link from the nth node to the middle 
        #[7]->[3]->[8]->[12] 
        #      m    nxt
        #[7]->[3]<-[8]<-[12] 

        while middle:
            nxt = middle.next 
            tmp  = None
            if middle.next and middle.next.next:
                tmp = middle.next.next                
                nxt.next = middle
            middle = tmp


        print("*"*32)
        while root:
            print(root.val)
        print("*"*32)
        #step3: hook nodes 

        return None


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
    s.reorder_list(ptr)

    r = None
    while r:
        print(r.val)
        r=r.next

    print ("END!")
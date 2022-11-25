
from utilities import MyUtilities, Node

class Solution:

    def swapPairs(self, root):
        
        dummy = Node(-1)
        dummy.next = root
        ptr = dummy
        
        while ptr and ptr.next:
            nxt1 = ptr.next
            nxt2 = nxt1.next #can be None

            if nxt2:
                nxt1.next = nxt2.next
                nxt2.next = nxt1
                ptr.next = nxt2
            
            ptr = nxt1

        return dummy.next


if __name__=='__main__':
    print ("Start...")
    
    n=[1,2,3,4,5,6,7,8,9,10]
    ptr = MyUtilities.build_linked_list(n)
    print ("BEFORE")
    MyUtilities.print_linked_list(ptr)

    s = Solution()
    ptr2 = s.swapPairs(ptr)

    print ("and AFTER:")
    MyUtilities.print_linked_list(ptr2)
    print ("END!")
from utilities import MyUtilities 

class Solution:

    def reversed(self, root):
        
        prv = None
        while root:
            nxt = root.next
            root.next = prv
            prv = root
            root = nxt

        return prv


if __name__=='__main__':
    print ("start")

    print ("BEFORE")
    n = [1,4,7,2,3,6,8,9,1,0,12,15,66]
    ptr = MyUtilities.build_linked_list(n)
    MyUtilities.print_linked_list(ptr)

    s = Solution()
    head = s.reversed(ptr)

    print ("AFTER")
    MyUtilities.print_linked_list(head)

    print ("END")
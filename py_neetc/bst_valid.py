from utilities import MyUtilities

class Solution:

    def is_valid(self, root):
        
        return False 


if __name__=='__main__':
    print ("Start...a")

    ptr = MyUtilities.build_bst([4,6,1,0,12,15,16,20,11])
    MyUtilities.print_tree(ptr)

    s = Solution()
    r = s.is_valid(ptr) 
    print ('r:=',r)
    print ("END!")
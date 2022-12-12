from utilities import MyUtilities 

class Solution:

    def is_subtree(self, r1,r2):
        
        def dfs(h1, h2):
            if not h1 and not h2:
                return True
            if not h2 or not h1:
                return False

            same_val = h1.val == h2.val
            if same_val:
                is_left = dfs(h1.left, h2.left)
                is_right = dfs(h1.right, h2.right)
                return is_left and is_right
            
            return same_val
        
        #get value of subRoot = value of root
        res = []
        def dfs_ptr_to_value(ptr):
            if not ptr:
                return 
                        
            if ptr.val==r2.val:
                res.append(ptr)
            
            dfs_ptr_to_value(ptr.left)                        
            dfs_ptr_to_value(ptr.right)            
        
        dfs_ptr_to_value(r1) 
        if not res:
            return False
        for ptr in res:
            f = dfs(ptr,r2)
            if f:
                return True
        return False

            


if __name__=='__main__':
    print ("start")

    print ("BEFORE")
    n1 = [1,1]
    n2 = [1]
    ptr1 = MyUtilities.build_tree(n1)
    ptr2 = MyUtilities.build_tree(n2)
    
    MyUtilities.print_tree(ptr1)
    print ("_#_"*32)
    MyUtilities.print_tree(ptr2)

    s = Solution()
    f = s.is_subtree(ptr1,ptr2)
    print ("f:=",f)
    print ("END")
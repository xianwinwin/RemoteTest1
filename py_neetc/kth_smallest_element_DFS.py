from utilities import MyUtilities
from collections import deque

class Solution:

    def kth_element(self, root, kth):
        
        levels = []
        def dfs(node): 
            if not node:
                return None
            
            dfs(node.left)
            levels.append(node.val)
            if len(levels)>=kth:
                return None

            dfs(node.right)            

        dfs(root)
        print("levels:=",levels)
        return levels[kth]        

         
if __name__=='__main__':
    print ("Start...a")
    
    nums = [3,1,4,2,9,10,12,14,15,16,19,100,102,104,22]
    root = MyUtilities.build_bst(nums)
    MyUtilities.print_my_tree(root)
    print ("*"*32)
    s = Solution()
    r = s.kth_element(root,1) 
    print ('r:=',r)
    print ("END!")
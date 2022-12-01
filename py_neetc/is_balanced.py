#https://leetcode.com/problems/balanced-binary-tree/

from utilities import MyUtilities
from collections import defaultdict

class Solution:
    def isBalanced(self, root) -> bool:
        
        depth = {}        
        def dfs(dive_counter, node):
            if not node:
                depth[dive_counter]=dive_counter
                return 
            
            dfs(dive_counter, node.left)
            dfs(dive_counter, node.right)            
            
        dfs(0,root)
        print (depth)


        return False

if __name__=='__main__':
    print ("START")

    root = MyUtilities.build_tree( [1,2,2,3,3,None,None,4,4])
    MyUtilities.print_tree(root, init_space=5)

    low = 14
    high = 34
    s = Solution()
    r = s.isBalanced(root)
    print ("is symmetric?:=",r)

    print ("END")

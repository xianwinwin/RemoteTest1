#https://leetcode.com/problems/balanced-binary-tree/

from utilities import MyUtilities
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        
        res = [True]
        def dfs(node):
            if not node:  
                return 0
            
            left = dfs(node.left) 
            right = dfs(node.right)            

            if abs(left-right)>1:
                res[0]=False 
            return 1+max(left,right)
                
        dfs(root)  
        return res[0]

if __name__=='__main__':
    print ("START")

    n = [8,6,2,9,3,None,None,4,12]   
    root = MyUtilities.build_tree( n )
    MyUtilities.print_tree(root, init_space=5)


    low = 14
    high = 34
    s = Solution()
    r = s.isBalanced(root)
    print ("is symmetric?:=",r)

    print ("END")

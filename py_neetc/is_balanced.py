#https://leetcode.com/problems/balanced-binary-tree/

'''
Given a binary tree, determine if it is height-balanced.

Definition: height-balanced binary tree is a binary tree in which the depth of the two 
            subtrees of every node never differs by more than one.

https://www.youtube.com/watch?v=QfJsau0ItOY
'''

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

    n = [8,6,2,9,3,7,None,4,12,None,None,None,None,11]   
    root = MyUtilities.build_tree( n )
    MyUtilities.print_my_tree(root)


    low = 14
    high = 34
    s = Solution()
    r = s.isBalanced(root)
    print ("is isBalanced?:=",r)

    print ("END")

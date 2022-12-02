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
        
        def dfs(node):
            if not node:  
                return [True,0]
            
            left = dfs(node.left) 
            right = dfs(node.right)            

            f1 = left[0] and right[0] 
            f2 = abs(left[1]-right[1])<=1
            is_blanced = f1 and f2
            return [is_blanced, 1+max(left[1],right[1])]
                
        v = dfs(root)  
        return v[0]

if __name__=='__main__':
    print ("START")

    #n = [8,6,2,9,3,None,None,4,12]
    #n = [1,2,3,4,5,6,None,8]
    #root = MyUtilities.build_tree( n )
    #MyUtilities.print_tree(root, init_space=5)
    
    n8 = TreeNode(8)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n12 = TreeNode(12)

    n8.left=n6
    n8.right=n2
    n6.left = n9
    n6.right = n3
    n9.left = n4
    n9.right= n12

    root = n8


    low = 14
    high = 34
    s = Solution()
    r = s.isBalanced(root)
    print ("is symmetric?:=",r)

    print ("END")

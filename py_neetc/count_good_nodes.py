#https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

'''
from utilities import MyUtilities

class Solution:

    def goodNodes(self, root):
        
        res = [0]
        def dfs(node, max_value):
            if not node:
                return 
            
            if node.val>=max_value:
                res[0]=res[0]+1
            max_value = max(node.val,max_value)

            dfs(node.left, max_value)
            dfs(node.right, max_value)
            
        dfs(root, root.val)
        return res[0]
    
if __name__=='__main__':
    print ("Start...")
    n = [3,1,4,3,None,1,5]
    n = [9,None,3,6]
    n = [3,3,None,4,2]
    n = [2,None,4,10,8,None,None,4]
    ptr = MyUtilities.build_tree(n)
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    r = s.goodNodes(ptr) 
    print ('r:=',r)
    print ("END!")
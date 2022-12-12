#https://leetcode.com/problems/diameter-of-binary-tree/
'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''
from utilities import MyUtilities

class Solution:

    def depth(self, root):
        
        r = [0]
        def dfs(n):
            if not n:
                return 0
            
            left =  dfs(n.left)
            right =  dfs(n.right)
 
            r[0] = max(r[0],left+right)
            print ("left:=",left,'right:=',right)
            print ('sum left+right --->',left+right)
            print ('b--->',max(left,right)+1)
            print ("return max:",max(left,right) + 1)
            
            #why max? because it has 2 branches LEFT and RIGHT and we want the maximum depth
            return max(left,right) + 1 #adding one for the next; 

        dfs(root)
        return r[0]


if __name__=='__main__':
    print ("Start...a")

    n = [4,6,1,0,12,15,16,20,11]
    #n = [1,2]
    ptr = MyUtilities.build_bst(n)
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    r = s.depth(ptr) 
    print ('r:=',r)
    print ("END!")
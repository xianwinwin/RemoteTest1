#https://leetcode.com/problems/find-duplicate-subtrees/
'''
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
'''

from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def findDuplicateSubtrees(self, root):

        d = {}
        res = []         
        def dfs(path, node):
            if not node:
                return '#'
            
            my_range = []
            my_range.append(str(node.val))
            my_range.append(dfs(path, node.left))
            my_range.append(dfs(path, node.right))
            
            print (my_range)
            path += ','.join(my_range)
            if d.get(path,None):
                d[path]=d[path]+1
                
                if d[path]==2:
                    res.append(node) #add the nodes that are duplicated
            else:
                d[path]=1 
            return path
            
        dfs('',root) 
        return res


if __name__=='__main__':
    print ("Start...")

    n = [1,2,3,4,None,2,4,None,None,4]
    #n = [1,2,3,4,None,5,9,None,None,7]
    #n = [1,2,3,8,None,2,4,None,None,7]
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    levels = s.findDuplicateSubtrees(ptr) 
    for l in levels:
        print ('*'*32)
        MyUtilities.print_my_tree(l)            
    print ("END!")
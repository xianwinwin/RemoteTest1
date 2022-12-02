from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def findDuplicateSubtrees(self, root):

        d = {}
        res = []         
        def dfs(path, node):
            if not node:
                return '#'
            
            my_range = [str(node.val), dfs(path, node.left), dfs(path, node.right)]
            
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
    #n = [1,2,3,8,None,2,4,None,None,7]
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_tree(ptr, init_space=8)

    s = Solution()
    levels = s.findDuplicateSubtrees(ptr) 
    for l in levels:
        print ('<>'*8)
        MyUtilities.print_tree(l, init_space=8)            
    print ("END!")
from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def analysis(self, root):
        
        res = []
        def dfs(node):
            if not node:
                return None
            n = node.val
            l = dfs(node.left) 
            r = dfs(node.right)
            print (node.val,'--->',(n,l,r))
            return node.val
                
        dfs(root)
        return []


if __name__=='__main__':
    print ("Start...x")

    n = [1,8,7,4,2,3,9,11,12,22,5] 
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_tree(ptr, init_space=5)

    s = Solution()
    s.analysis(ptr)  
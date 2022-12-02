from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def analysis(self, root):
        
        res = []
        def dfs(node):
            if not node:
                return 0

            m = [ node.val, dfs(node.left), dfs(node.right) ]
            print (m,'-->', sum(m))
            return sum(m)
                
        dfs(root)
        return []


if __name__=='__main__':
    print ("Start...x")

    n = [1,8,7,4,2,3] 
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_tree(ptr, init_space=5)

    s = Solution()
    s.analysis(ptr)  
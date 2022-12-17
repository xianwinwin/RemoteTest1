from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def analysis(self, root):
        
        res = [0]
        def dfs(node): 
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right) 
            
            sum_sub_tree = node.val + left + right

            return sum_sub_tree

        v = dfs(root)
        return v


if __name__=='__main__':
    print ("Start...x")

    n = [1,8,7,4,2,3,9,11,12,22,5] 
    #n = [1,2,3,4,5]
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    v = s.analysis(ptr)  
    print ("v:=",v)
from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def hasPathSum(self, root, targetSum):
        path_values = []
        res = [False]

        def dfs(node, leaf):
            if not node:
                if leaf and targetSum==sum(path_values):
                    res[0] = True 
                return 0
            
            path_values.append(node.val)
            is_leaf = not node.left and not node.right
            dfs(node.left, is_leaf)
            dfs(node.right, is_leaf) 
            if path_values:
                path_values.pop()
            
        dfs(root, (not root.left and not root.right))

        return res[0]
 


if __name__=='__main__':
    print ("Start...")

    targetSum = 21
    n = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    #n = [1,2]
    ptr = MyUtilities.build_tree(n)    
    MyUtilities.print_tree(ptr, init_space=5)

    s = Solution()
    r = s.hasPathSum(ptr, targetSum)  
    print ("Result:=",r)
from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def get_depth(self, root):
        
        cache  = defaultdict(list)
        def dfs(depth, node):
            if not node:
                return
            
            cache[depth].append(node.val)
            dfs(depth+1, node.left)
            dfs(depth+1, node.right)
        
        dfs(0,root)
        return cache


if __name__=='__main__':
    print ("Start...")

    ptr = MyUtilities.build_tree([4,6,1,0,12,15,16,20,11])
    MyUtilities.print_tree(ptr)

    s = Solution()
    levels = s.get_depth(ptr) 
    print (levels)
    print ("END!")
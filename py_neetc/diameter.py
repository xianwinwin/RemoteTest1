from utilities import MyUtilities

class Solution:

    def depth(self, root):
        
        r = [0]
        def dfs(n):
            if not n:
                return 0
            
            left = 1 + dfs(n.left)
            right = 1 + dfs(n.right)
            max_depth = max(left,right)
            r[0] = max(r[0],max_depth)
            return max(r[0],max_depth)

        dfs(root)
        return r[0]


if __name__=='__main__':
    print ("Start...a")

    ptr = MyUtilities.build_bst([4,6,1,0,12,15,16,20,11])
    MyUtilities.print_tree(ptr)

    s = Solution()
    r = s.depth(ptr) 
    print ('r:=',r)
    print ("END!")
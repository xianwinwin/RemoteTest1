from utilities import MyUtilities

class Solution:

    def is_valid(self, root):

        res = [True]

        def dfs(node, value_left, value_right):
            if not node:
                return
            
            node_value = node.val
            if not value_left<node_value<value_right:
                res[0]=False
                return #no need to continue checking
            
            dfs(node.left, value_left, node_value)
            dfs(node.right, node_value, value_right)

        dfs(root,float('-inf'),float('inf'))
        return res[0] 


if __name__=='__main__':
    print ("Start...a")

    #ptr = MyUtilities.build_bst([4,6,1,0,12,15,16,20,11])
    ptr = MyUtilities.build_tree([4,6,1,0,12,15,16,20,11])
    MyUtilities.print_tree(ptr)

    s = Solution()
    r = s.is_valid(ptr) 
    print ('r:=',r)
    print ("END!")
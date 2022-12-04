from utilities import MyUtilities

class Solution:

    '''
    remove node from parent only if:
    1. child is 0 AND both childs are 0 OR
    2. child id 0 AND both childs are NONE
    '''

    def pruneTree(self, root):

        def dfs(node, partent_node, direction):
            if not node:
                return
            
            #option 1
            if node.val==0 and node.left and node.left.val == 0 and node.right and node.right.val == 0:
                if direction=='left':
                    partent_node.left = None
                if direction=='right':
                    partent_node.right = None
                return
            
            #option 2:
            if node.val==0 and not node.left and not node.right:
                if direction=='left':
                    partent_node.left = None
                if direction=='right':
                    partent_node.right = None
                return
            
            dfs(node.left, node, 'left')
            dfs(node.right, node, 'right')

        dfs(root, root, '')
        return root


if __name__=='__main__':
    print ("start...")

    n = [1,0,1,0,0,0,1]
    
    ptr = MyUtilities.build_tree(n)
    MyUtilities.print_tree(ptr, init_space=2)

    s = Solution()
    r = s.pruneTree(ptr)

    print ("AFTER...")
    MyUtilities.print_tree(r, init_space=2)

    print ("END")
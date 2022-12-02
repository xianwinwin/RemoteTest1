#https://leetcode.com/problems/construct-string-from-binary-tree/submissions/
#https://www.youtube.com/watch?v=b1WpYxnuebQ

from utilities import MyUtilities


class Solution:

    def tree2str(self, root) -> str:

        res = []
        def dfs(node):
            if not node:
                return
            
            res.append('(')
            res.append(str(node.val))
            
            #per request: except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
            #Input: root = [1,2,3,null,4]
            #expected Output: "1(2()(4))(3)"
            if not node.left and node.right: 
                res.append('()')
                
            dfs(node.left)
            dfs(node.right)
            res.append(')')

        dfs(root)
        return ''.join(res)[1:-1]

if __name__=='__main__':
    print ("Start...")
    
    ptr = MyUtilities.build_tree([1,2,3,None, 4])
    MyUtilities.print_tree(ptr, init_space=10)
    print ("*"*32)

    s = Solution()
    r = s.tree2str(ptr)
    print (r)
    print ("END")
      


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
        

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    root = n1
    return root


if __name__=='__main__':
    print ("Start...a")
    
    ptr = get_root2()

    s = Solution()
    r = s.depth(ptr) 
    print ('r:=',r)
    print ("END!")
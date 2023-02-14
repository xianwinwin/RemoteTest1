from datetime import datetime

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def tree_sum(self, t1, t2, target):
        
        #get value X from t1
        res = []
        def dfs_x(n):
            if not n:
                return 

            if n.val>target:
                return

            dfs_x(n.left)
            dfs_x(n.right)

            dfs_y(t2, target-n.val)
            if res:
                return res

        
        #check if the missing number Y: target-X is in t2
        def dfs_y(n, new_target):
            if not n:
                return 
            
            if n.val == new_target:
                res.append( (n.val, target-new_target) )
                return

            dfs_y(n.left, new_target)
            dfs_y(n.right, new_target)
        

        dfs_x(t1)
        return res

if __name__=='__main__':
    print ("Start...")    

    #t1
    n6 = TreeNode(6)
    n3 = TreeNode(3)
    n17 = TreeNode(17)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n11 = TreeNode(11)
    n19 = TreeNode(19)

    n6.left = n3
    n6.right = n17
    n3.left = n0
    n3.right = n4
    n17.left = n11
    n17.right = n19

    #t2
    n8 = TreeNode(8)
    n5 = TreeNode(5)
    n13 = TreeNode(13)
    n1 = TreeNode(1)
    n7 = TreeNode(7)

    n8.left=n5
    n8.right=n13
    n5.left=n1
    n5.right=n7

    t1 = n6
    t2 = n8
    target = 30

    s = Solution()
    res = s.tree_sum(t1,t2,target)  
    print ('res:=',res)
    print ("END")
 
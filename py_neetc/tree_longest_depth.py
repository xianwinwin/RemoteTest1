#https://www.youtube.com/watch?v=bkxqA8Rfv04
#Diameter of a Binary Tree - Leetcode 543 - Python

class Node():
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def get_dpeth(self, root):
        res = [0]

        def dfs(p):
            if not p:
                return 0 #return the height
            
            left = dfs(p.left)
            right = dfs(p.right)
            d =  left + right
            res[0] = max(res[0], d) #calc longest diameter
            return 1 + max(left, right) #height: you return either side that is the longest

        dfs(root)
        return res[0]

    def print_tree(self,ptr):
       
        levels = []
        def dfs(p):
            if not p:
                return None
            
            dfs(p.left)
            levels.append(p.val)
            dfs(p.right)
        
        dfs(ptr)
        return levels
            
def get_root1():
    '''
                    1
                2      3
             4    5
          6         7
         8 9       10 
    '''

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    n1.left  = n2
    n1.right = n3
    n2.left  = n4
    n2.right = n5
    n5.right = n7
    n7.left  = n10
    n4.left  = n6
    n6.left  = n8
    n6.right = n9

    root = n1
    return root


def get_root2():
    '''
                    1
                2      3
             4    5
    '''

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
    print ("start")


    root = get_root2()
    s = Solution()
    levels = s.print_tree(root)
    print (levels)
    depth = s.get_dpeth(root)
    print ("depth:=",depth)
    print ("END")
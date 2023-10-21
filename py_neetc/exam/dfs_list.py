from collections import defaultdict

class Node:
    
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val=val

    def __str__(self) -> str:
        return 'val:='+str(self.val)
     

class Simulation:
    
    def run(self, root):
        
        def dfs(node, level):
            if not node:
                return
            
            d[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        d = defaultdict(list)
        dfs(root,0)
        return d

if __name__=='__main__':
    print ('start...')
    
    n1 = Node(1)
    n2 = Node(4)
    n3 = Node(8)
    n4 = Node(9)
    n5 = Node(2)
    n6 = Node(200)
    
    n1.left = n2
    n1.right = n3
    n3.left=n4
    n3.right=n5
    n4.left=n6
    s = Simulation()
    res = s.run(n1)  
    print (res)
    print ("end")



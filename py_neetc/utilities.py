from collections import defaultdict

class Node:

    def __init__(self, val):
        self.val=val
        self.next = None


class TreeNode():
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MyUtilities:

    @staticmethod
    def get_tree(ptr, req='pre_order'):
        levels = []
        
        def dfs(n):
            if not n:
                return
            
            if req=='pre_order':
                levels.append(n.val)
                dfs(n.left)            
                dfs(n.right)

            elif req=='inorder':            
                dfs(n.left)  
                levels.append(n.val)          
                dfs(n.right)

            elif req=='post_order':
                dfs(n.left)                   
                dfs(n.right)
                levels.append(n.val)   
            
            else:
                raise ValueError("requested type can be either: [pre_order,inorder or post_order] but you requesed: ",req)

        dfs(ptr)
        return levels
        
    @staticmethod
    def build_bst(n):
        n.sort()

        def dfs(ary):
            if not ary:
                return None

            mid = len(ary)//2
            tn = TreeNode(ary[mid])
            tn.left = dfs(ary[0:mid])
            tn.right = dfs(ary[mid+1:])
            return tn

        ptr = dfs(n)
        return ptr


    @staticmethod
    def print_tree(ptr):
        d = defaultdict(list)

        my_depth = [0]

        def dfs(depth, n):
            if not n:
                d[depth].append(None)
                return None
            
            d[depth].append(n.val)
            my_depth[0] = max(my_depth[0],depth)
            dfs(depth+1, n.left)
            dfs(depth+1, n.right)

        dfs(0,ptr)
        max_level = my_depth[0]+1
        num_spots = len(d[max_level])*15

        h = len(d)        
        
        for _,v in d.items():
            line = ''
            for i in v:
                spaces = ' '*num_spots
                if not i:
                    i=''
                line += spaces+str(i)+spaces
            print(line)
            
            num_spots = num_spots//2

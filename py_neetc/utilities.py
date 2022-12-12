from collections import defaultdict
from collections import deque

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
    def build_linked_list(nums):

        last_node = None
        for i in range(len(nums)-1,-1,-1):
            n = Node(nums[i])
            n.next = last_node
            last_node = n

        return last_node    

    @staticmethod
    def print_linked_list(root):
        head = root
        my_list = []
        while head:
            my_list.append('['+str(head.val)+']')
            head=head.next
        
        print ('->'.join(my_list))

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
    def build_tree(n):
        if not n:
            return None

        dq = deque()
        
        tn = TreeNode(n[0])
        dq.append(tn)
        root = tn

        index = 0
        while dq:
            node = dq.popleft()

            if not node:
                continue

            index+=1

            if index>len(n)-1:
                break 
            
            node.left = TreeNode(n[index]) if n[index]==0 or n[index] else None
            index+=1

            if index>len(n)-1:
                break 

            node.right = TreeNode(n[index]) if n[index]==0 or n[index] else None

            dq.append(node.left)
            dq.append(node.right)          

        return root

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

        root = dfs(n)
        return root

    @staticmethod
    def print_my_tree(root, val="val", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)


    @staticmethod
    def print_tree(ptr, init_space=15):
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
        num_spots = len(d[max_level])*init_space
 
        for _,v in d.items():
            line = ''
            for i in v:
                spaces = ' '*num_spots
                if i!=0 and not i:
                    i=''
                line += spaces+str(i)+spaces
            print(line)
            
            num_spots = num_spots//2

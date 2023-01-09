from utilities import MyUtilities
from collections import defaultdict, deque

class Solution:

    def get_depth(self, root):
        
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            levels = []
            size_q = len(dq)
            for _ in range(0,size_q):
                node = dq.popleft()
                levels.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                
            if levels:
                res.append(levels)
        return res


if __name__=='__main__':
    print ("Start...")

    ptr = MyUtilities.build_tree([4,6,1,0,12,15,16,20,11])
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    levels = s.get_depth(ptr) 
    print (levels)
    print ("END!")
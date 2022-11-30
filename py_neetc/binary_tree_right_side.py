from utilities import MyUtilities
from collections import deque

class Solution:

    def rightSideView(self, root): 
        
        if not root:
            return []

        dq = deque()
        dq.append(root)
        res=[root.val]
        while dq:            
            dq_len = len(dq)            
            last_val = None
            for i in range(0,dq_len):
                node = dq.popleft()
                if node:

                    if node.left:
                        dq.append(node.left)
                        last_val = node.left.val
                    if node.right:
                        dq.append(node.right)
                        last_val = node.right.val
                        
            if last_val != None: #ok for 0   
                res.append(last_val)
        return res


if __name__=='__main__':
    print ("Start...a")
 
    #ptr = MyUtilities.build_tree([3,7,8,5,6,None, 9,3,4,None,None, None, None, None, None, 2,3])
    ptr = MyUtilities.build_tree([1,2,3,0])
    MyUtilities.print_tree(ptr, init_space=10)

    s = Solution()
    res = s.rightSideView(ptr) 
    print (res)

    print ("END!")
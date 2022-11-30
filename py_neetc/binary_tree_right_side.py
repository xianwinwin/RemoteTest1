from utilities import MyUtilities
from collections import deque

class Solution:

    def rightSideView(self, root): 
        
        dq = deque()
        dq.append(root)
        res = []
        res.append(root.val)
        while dq:            
            dq_len = len(dq)            
            for i in range(0,dq_len):
                node = dq.popleft()

                if node.left and node.left.val:
                    dq.append(node.left)

                if node.right and node.right.val:
                    dq.append(node.right)
                
                if i==dq_len-1 and node.right:
                    res.append(node.right.val)

        return res


if __name__=='__main__':
    print ("Start...a")
 
    ptr = MyUtilities.build_tree([3,7,8,5,6,None, 9,3,4,None,None, None, None, None, None, 2,3])
    MyUtilities.print_tree(ptr, init_space=10)

    s = Solution()
    res = s.rightSideView(ptr) 
    print (res)

    print ("END!")
from utilities import MyUtilities
from collections import deque

class Solution:

    def kth_element(self, root, kth):
        
        q = deque()
        q.append(root)
        cur = root

        n=0
        while q or cur:
            while cur:
                q.append(cur)
                cur=cur.left
            
            cur = q.pop()
            n+=1 
            if n==kth:
                return cur.val
            cur = cur.right
        
        return -1
 
if __name__=='__main__':
    print ("Start...a")
    
    nums = [18,22,54,3,6,15,7,1]
    root = MyUtilities.build_bst(nums)
    MyUtilities.print_tree(root)
    print ("*"*32)
    s = Solution()
    r = s.kth_element(root,3) 
    print ('r:=',r)
    print ("END!")
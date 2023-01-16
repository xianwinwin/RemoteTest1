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
    
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4

    root = MyUtilities.build_bst(nums)
    MyUtilities.print_my_tree(root)
    print ("*"*32)
    s = Solution()
    r = s.kth_element(root,k) 
    print ('r:=',r)
    print ("END!")
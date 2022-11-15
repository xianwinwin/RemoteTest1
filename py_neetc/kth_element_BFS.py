from utilities import MyUtilities
from collections import deque

class Solution:

    def kth_element(self, root, kth):
        
        q = deque()
        q.append(root)

        n=0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if n==kth:
                return node.val
            n+=1
        
        return -1

            

         
if __name__=='__main__':
    print ("Start...a")
    
    nums = [8,2,4,3,6,15,7,1]
    root = MyUtilities.build_bst(nums)
    MyUtilities.print_tree(root)
    print ("*"*32)
    s = Solution()
    r = s.kth_element(root,0) 
    print ('r:=',r)
    print ("END!")
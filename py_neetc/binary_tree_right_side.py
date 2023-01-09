from utilities import MyUtilities
from collections import deque

'''
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

'''

class Solution:

    def rightSideView(self, root): 
        
        if not root:
            return []

        dq = deque()
        dq.append(root)
        res=[root.val]
        while dq:            
            dq_len = len(dq)            
            last_val = None #this is the trick. It'll be overwriten it when looking to the right
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
  
    ptr = MyUtilities.build_tree([1,2,3,0,6,None,None, 7])
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    res = s.rightSideView(ptr) 
    print (res)

    print ("END!")
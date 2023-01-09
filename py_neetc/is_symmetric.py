from utilities import MyUtilities
from collections import deque


'''
https://leetcode.com/problems/symmetric-tree/
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution:
    def isSymmetric(self, root) -> bool:
        
        dq = deque()
        dq.append(root)

        while dq:
            len_dq = len(dq)
            levels  = []
            for i in range(0,len_dq):
                node = dq.popleft()
                if node.left:
                    levels.append(node.left.val)
                    dq.append(node.left)
                else:
                    levels.append(None)
                if node.right:
                    levels.append(node.right.val)
                    dq.append(node.right)
                else:
                    levels.append(None)
                    
            #check symetric on levels:
            m = len(levels)-1
            l = 0 
            for i in range(0,len(levels)//2):
                if levels[i]!=levels[m]:
                    return False
                m-=1

        return True

if __name__=='__main__':
    print ("START")

    root = MyUtilities.build_tree([1,2,2,3,4,4,3])
    MyUtilities.print_my_tree(root)
 
    s = Solution()
    r = s.isSymmetric(root)
    print ("is symmetric?:=",r)

    print ("END")

from utilities import MyUtilities
from collections import deque

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
    MyUtilities.print_tree(root, init_space=5)

    low = 14
    high = 34
    s = Solution()
    r = s.isSymmetric(root)
    print ("is symmetric?:=",r)

    print ("END")

class Node:

    def __init__(self, val):
        self.val=val
        self.next = None

class Solution:

    def kth_element(self, root, kth):
        return None


class Node():
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_root2():
    '''
                          15
                 12               23
             4      13
           2   5       14
        1          
    '''

    n15 = Node(15)
    n12 = Node(12)
    n23 = Node(23)
    n4 = Node(4)
    n13 = Node(13)
    n2 = Node(2)
    n5 = Node(5)
    n14 = Node(14)
    n1 = Node(1)
    
    n15.left=n12
    n15.right=n23
    n12.left=n4
    n12.right=n13
    n13.left = n14
    n4.left = n2
    n4.right = n5
    n2.left = n1
    
    return root


if __name__=='__main__':
    print ("Start...a")
    
    ptr = get_root2()

    s = Solution()
    r = s.kth_element(ptr,4) 
    print ('r:=',r)
    print ("END!")
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
                    1
                2      3
             4    5
    '''

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    root = n1
    return root


if __name__=='__main__':
    print ("Start...a")
    
    ptr = get_root2()

    s = Solution()
    r = s.kth_element(ptr,4) 
    print ('r:=',r)
    print ("END!")
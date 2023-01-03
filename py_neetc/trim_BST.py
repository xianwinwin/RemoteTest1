#https://leetcode.com/problems/trim-a-binary-search-tree/

'''
Given the root of a binary search tree and the lowest and highest boundaries 
as low and high, trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements 
that will remain in the tree (i.e., any node's descendant should remain a descendant). 
It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change 
depending on the given bounds.
'''

from utilities import MyUtilities

class Solution:
    def trimBST(self, root, low, high):
        
        def dfs(node):
            if not node:
                return

            if node.val > high:
                return dfs(node.left)
            elif node.val < low:
                return dfs(node.right)
            else:
                #node.left = dfs(node.left)
                #node.right = dfs(node.right)
                return node

        return dfs(root)


if __name__=='__main__':
    print ("START")

    root = MyUtilities.build_bst([1,5,7,22,16,34,4,14,3])
    MyUtilities.print_my_tree(root)

    low = 14
    high = 34
    s = Solution()
    r = s.trimBST(root, low, high)
    print ("\n\nAFTER\n")
    MyUtilities.print_my_tree(r)

    print ("END")
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
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        return dfs(root)


if __name__=='__main__':
    print ("START")

    root = MyUtilities.build_bst([1,5,7,22,16,34,4,14,3])
    MyUtilities.print_tree(root, init_space=10)

    low = 14
    high = 34
    s = Solution()
    r = s.trimBST(root, low, high)
    print ("AFTER")
    MyUtilities.print_tree(r, init_space=10)

    print ("END")
#https://leetcode.com/problems/path-sum-iii/
'''
Given the root of a binary tree and an integer targetSum, return the number of paths where 
the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).

 
'''
from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def pathSum(self, root, targetSum):
        
        self.count = 0
        freq = {0:1}
        def dfs(node, ps):
            if not node: 
                return 

            cs = ps + node.val
            x = cs - targetSum
            if x in freq:
                self.count += freq[x]
            if cs in freq:
                freq[cs]+=1
            else:
                freq[cs]=1

            dfs(node.left, cs)
            dfs(node.right, cs)
            freq[cs]=-1

        dfs(root, 0)
        return self.count


if __name__=='__main__':
    print ("Start...x")

    n = [10,5,-3,3,2,None,11,3,-2,None,1]
    #n = [10,1,2,7,6,1,5]
    targetSum = 8
    ptr = MyUtilities.build_tree(n)
    MyUtilities.print_my_tree(ptr)

    s = Solution()
    v = s.pathSum(ptr, targetSum)  
    print ("v:=",v)
'''
https://leetcode.com/problems/most-frequent-subtree-sum/
Given the root of a binary tree, return the most frequent subtree sum. 
If there is a tie, return all the values with the highest frequency in any order.
The subtree sum of a node is defined as the sum of all the node values formed by 
the subtree rooted at that node (including the node itself).

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def findFrequentTreeSum(self, root):

        if not root:
            return []

        d = {} #Key=sum, V = freq

        def dfs(node):
            if not node:
                return 0

            sum_sub_tree = sum([node.val, dfs(node.left), dfs(node.right)])            
            freq = d.get(sum_sub_tree,0)
            d[sum_sub_tree] = freq+1

            return sum_sub_tree
        
        dfs(root) 

        freq = []
        for k,v in d.items(): #k=sum, v=freq
            freq.append( (v,k) )
        freq.sort(key = lambda x: x[0], reverse=True)
        
        most_freq = freq[0][0]
        res = [freq[0][1]]    
        for ptr in freq[1:]:
            if ptr[0]==most_freq:
                res.append(ptr[1])
            else:
                break

        return res
        

if __name__=='__main__':
    print ("Start...")
 
    s = Solution()

    n1 = TreeNode(5)
    n2 = TreeNode(2)
    n3 = TreeNode(-5)
    n1.left=n2
    n1.right=n3

    root = n1 
    r = s.findFrequentTreeSum(root) 
     
    print ('findFrequentTreeSum:=',r)

    print ("END!")
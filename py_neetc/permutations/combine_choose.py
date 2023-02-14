'''
https://leetcode.com/problems/combinations/description/

77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
'''

class Solution:

    def combine(self, n, k):        
        
        res = set()
        nums = [i+1 for i in range(0,n)]        

        def dfs(index, combo): 
            if len(combo)==k:
                combo.sort() 
                if tuple(combo) not in res:
                    res.add(tuple(combo[:]))
                return 
            
            #when you do it like this, you will have any combo (think: at one point 
            #number 2 will be the first one in the combo)
            for i in range(index,len(nums)):
                combo.append(nums[i])
                dfs(i+1, combo)
                combo.pop()

        dfs(0,[])

        return list(res)



if __name__=='__main__':
    print ("Start...")

    k=2
    n=4
    s = Solution()    
    perms = s.combine(n,k) 
    
    for p in perms:
        print (p)

    print ('len:=',len(perms))  
    print ("END!")
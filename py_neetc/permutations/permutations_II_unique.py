'''
https://leetcode.com/problems/permutations-ii/description/
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''

class Solution:

    def permuteUnique(self, nums):

        res = set()

        #creating a unique set of permutations for indexes [[1,2,3],[1,3,2]...]
        indexes = [i for i in range (0, len(nums))]        

        def dfs(combo):
            if len(combo)==len(indexes):
                
                new_combo = []
                for i in combo:
                    new_combo.append(nums[i]) #add the value of nums [nums[i]] so ok to have duplicates [1,1,2]
                
                if tuple(new_combo) not in res:
                    res.add( tuple(new_combo) )
                return
            
            for n in indexes:
                if n not in combo:
                    combo.append(n)
                    dfs(combo)
                    combo.pop()

        dfs([])

        return list(res)



if __name__=='__main__':
    print ("Start...")

    nums = [1,1,2]
    s = Solution()    
    perms = s.permuteUnique(nums) 
    
    for p in perms:
        print (p)

    print ('len:=',len(perms))  
    print ("END!")
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

        res = []
        
        def dfs(index, combo):
            if len(combo)==len(nums):
                res.append(combo[:])
                return 

            v = nums[index]
            new_list = [v] + nums[0:index] + nums[index+1:len(nums)]
            print (new_list)
            for n in new_list:
                combo.append(n)
                dfs(index+1,combo)
                combo.pop()

        dfs(0,[])

        return res



if __name__=='__main__':
    print ("Start...")

    nums = ['a','a','b']
    s = Solution()    
    perms = s.permuteUnique(nums) 
    
    for p in perms:
        print (p)

    print ('len:=',len(perms))  
    print ("END!")

''' 
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

'''

from collections import defaultdict

class Solution:
    def threeSum(self, nums):
        
        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        res = set()

        nums.sort()

        def two_sum(l,target):
            r = len(nums)-1
            while l<r:
                two_sum = nums[l]+nums[r]
                if two_sum==target:
                    return [nums[l],nums[r]]
                if two_sum>target:
                    r-=1
                else:
                    l+=1
            return []

        for ia in range(0,len(nums)-1):
            a = nums[ia]
            target = a*(-1)
            values = two_sum(ia+1,target)
            if values:
                values.append(a)                
                res.add(tuple(sorted(values)))

        return list(res) 

if __name__=='__main__':
    print ("START") 
 
    nums = [-1,0,1,2,-1,-4]
    
    s = Solution()
    res = s.threeSum(nums)    
    print ("Res:=",res)

    print ("END")

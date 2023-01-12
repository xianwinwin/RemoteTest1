'''
https://leetcode.com/problems/maximum-subarray/
https://www.youtube.com/watch?v=5WZl3MMT0Eg
Maximum Subarray: Given an integer array nums, find the 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

''' 

class Solution:

    def maxSubArray(self,nums):

        if len(nums)==0:
            return -1

        global_max = nums[0]
        cur_max = nums[0]

        for n in nums[1:]:
            
            # add it to cur_max or reset to n
            if cur_max+n>n:
                cur_max=cur_max+n
            else:
                cur_max=n
            
            global_max = max(cur_max,global_max)

        return global_max
 

if __name__=='__main__':
    print ("start...")
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()     
    r = s.maxSubArray(nums)
    print ("max subarray:=",r)

    print ("END!")
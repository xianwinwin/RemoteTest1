'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated 
at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of 
target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:

    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:

            mid = left + (right-left)//2
            mid_val =  nums[mid]

            if nums[mid]==target:
                return mid

            #left side is sorted correctly?
            if nums[left]<=mid_val:
                if target>mid_val or target <nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target<mid_val or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1

        return -1

if __name__=='__main__':
    print ('start...')

    nums =[1]
    target = 0

    #nums =[4,5,6,7,0,1,2]
    #target = 3

    #nums =[4,5,6,7,0,1,2]
    #target = 0

    nums =[7,8,20,25,1,3,5,6]
    target = 20

    nums =[3,1]
    target = 1

    s = Solution()
    res = s.search(nums,target)
    print (res)
    print ("END ")
 
'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:

    def searchRange(self, nums,  target):
        
        left, right = 0, len(nums)-1

        found_it = False
        while left<=right:

            mid_index = left + (right-left)//2

            if nums[mid_index]==target: 
                found_it = True
                break
            
            if nums[mid_index]<target:
                left = mid_index+1
            else:
                right = mid_index-1
        
        if not found_it:
            return [-1,-1]
        
        
        right = 0
        pos = 1
        
        while len(nums)>mid_index+pos and nums[mid_index+pos]==target:
            right+=1
            pos+=1

        left = 0
        pos=-1
        while mid_index+pos>=0 and nums[mid_index+pos]==target:
            left-=1
            pos-=1

        #return [mid_index-left:mid_index+right]
        left = mid_index+left
        right = mid_index+right
        return [left,right]

        
if __name__=='__main__':
    print ('start...')

    nums = [5,7,7,8,8,10]
    target = 8

    s = Solution()
    res = s.searchRange(nums,target)
    print (res)
    print ("END ")
 
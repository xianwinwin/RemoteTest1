'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such 
that each unique element appears at most twice. The relative order of the elements should be kept the same.

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


'''

class Solution:
    def removeDuplicates(self, nums):
 
        #step1: replace over 2 items witha a downder _
        ptr = None
        for i in range(0,len(nums)):
            prv = nums[i-1] if i>0 else None
            cur = nums[i]
            nxt = nums[i+1] if i+1<len(nums) else None
            
            if prv==None or nxt==None:
                continue 
            
            #the magic: when the last item (has over 2 items is the same as the next one - move on with _)
            if nxt==ptr:
                nums[i+1]='_'
                continue
            ptr = None
            
            if prv==cur==nxt:
                nums[i+1]='_'
                ptr = cur
            
        #step2: move downder to the left
        for i in range(0,len(nums)):
            if nums[i]=='_':
                for x in range (i,len(nums)):
                    if nums[x]!='_':
                        #switch #1
                        nums[i], nums[x] = nums[x], nums[i]
                        #switch #2 (if applicable)
                        if x>len(nums):
                            if nums[i+1]=='_' and nums[x+1]!='_':
                                nums[i+1], nums[x+1] = nums[x+1], nums[i+1]
                        break

        k=0
        for i in range(0,len(nums)):
            if nums[i]!='_':
                k+=1
            else:
                break

        return k, nums


if __name__=='__main__':
    print ("Start")
 
    nums = [0,0,0,0,0]
    s = Solution()     
    k, res = s.removeDuplicates(nums)
    print ("k:= ",k)
    print ("Res:= ",res)
    
    print ("END")
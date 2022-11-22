#https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
#see image to understand what needs to be done

class Solution:

    def nextPermutation(self, nums):

        #find pivot
        pivot = 0
        for i in range (len(nums)-1,-1,-1):
            if nums[i-1]<nums[i]:
                pivot = i
                break

        if pivot==0:
            return nums.sort()

        #swap pivot with the least number from the right

        #A. find the candidate to swap with: that is pivot-1 > number for the right of nums        
        ptr = len(nums)-1
        while nums[pivot-1]>=nums[ptr]:
            ptr -=1

        #B. swap with ptr
        nums[pivot-1], nums[ptr] = nums[ptr], nums[pivot-1] 

        #sort from pivot to the right 
        nums[pivot:] = sorted(nums[pivot:])                
        
        
 
if __name__=='__main__':
    print ("Start...")    

    s = Solution()

    #nums = [1,3,2] #[1,4,1,2,3,3,5]
    nums = [0,1,2,5,3,3,0]
    print (nums)
    s.nextPermutation(nums) 
    print ('answer:')
    print (nums)

    print ("END!")
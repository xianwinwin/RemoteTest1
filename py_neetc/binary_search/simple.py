'''
just checking how would it look like if we want an item close to target
'''
 
class Solution:

    def get_value(self, nums: int, target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + (r-l)//2
            if nums[m]==target:
                return nums[m]
            if nums[m]>target:
                r=m-1
            else:
                l=m+1
            
        return m


if __name__=='__main__':
    print ('start...')

    s = Solution()

    nums = [1,6,9,12,14,23,24,25,26,30,31,32,33,37,41,44,45,55]
    target = 46
    res = s.get_value(nums,target)
    print (res) 
    print ("END ")
 
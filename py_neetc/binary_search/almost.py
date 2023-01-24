'''
just checking how would it look like if we want an item close to target
'''
 
class Solution:

    def get_almost(self, nums: int, target: int, req_type='exact') -> int:
        
        l,r=0,len(nums)-1

        while (l<=r):

            mid = l + (r-l)//2
            if nums[mid]==target:
                return nums[mid]
            
            if nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        
        if req_type=='near_left':
            return nums[r]
        
        if req_type=='near_right':
            return nums[l]
        
        #exact
        return -1



if __name__=='__main__':
    print ('start...')

    s = Solution()

    nums = [1,6,9,12,14,23,24,25,26,30,31,32,33,37,41,44,45,55]
    target = 20
    req_type = 'near_right'
    res = s.get_almost(nums,target, req_type)
    print (res) #return 23
    print ("END ")
 
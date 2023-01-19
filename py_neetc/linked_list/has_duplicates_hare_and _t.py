

class Solution:
    def findDuplicate(self, nums):

        slow = nums[0]
        fast = nums[nums[0]]

        #find the virtual position for which slow should be located
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        # found that there's s dup. start from 0 until you find slow
        # slow and tmp moves on the same speed
        tmp = nums[0]
        while tmp!=nums[slow]:
            tmp = nums[tmp]
            slow = nums[slow]
        return tmp


if __name__=='__main__':
    print ("Start")

    nums = [2,5,9,6,9,3,8,9,7,1]   

    s = Solution()
    dup = s.findDuplicate(nums)
    print ("\nDuplicte:=",dup)


    print ("END")
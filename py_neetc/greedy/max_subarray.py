

class Solution:

    def get_max(self, nums):
        
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum += n
            max_sum = max(max_sum,cur_sum)

        return max_sum



if __name__=='__main__':
    print ("Start...")

    s = Solution()
    v = s.get_max(nums=[-2,1,-3,4,-1,2,1,-5,4])
    print ("MAX:=",v)

    print ("END")
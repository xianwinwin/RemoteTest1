import sys
import os
from datetime import datetime

class Solution:

    def permutations(self, nums):

        res = []
        def dfs(combo):
            if len(combo)==len(nums):
                res.append(combo[:])
                return 
             
            for e in nums:
                if e not in combo:
                    combo.append(e)
                    dfs(combo)
                    combo.pop()

        dfs([])
        return res
        
 
if __name__=='__main__':
    print ("Start...")
    start = datetime.now()

    s = Solution()

    nums = [1,2,3,4,5]
    perms = s.permutations(nums) 
    
    for p in perms:
        print (p)

    print ('len:=',len(perms))
    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)
    print ("END!")
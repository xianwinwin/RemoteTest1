#https://www.youtube.com/watch?v=REOH22Xwdkk
#Subsets - Backtracking - Leetcode 78
from datetime import datetime

class Solution:

    def subsets(self, nums):
        
        res = []        
        def dfs(index,combo):
            if index==len(nums): #stop case when the index has arrived to the end of the nums [1,2,3] (len=3)
                res.append(combo[:])
                return
                                
            combo.append(nums[index]) #add item
            dfs(index+1,combo)
            combo.pop() #do not include item
            dfs(index+1,combo)

        dfs(0,[])
        return res
        
        
if __name__=='__main__':
    print ("Start...")    
    start = datetime.now()

    s = Solution()

    nums = [1,2,3]
    sets = s.subsets(nums)  
    for s in sets:
        print (s)
    print("len:=",len(sets))

    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)

    print ("END!")
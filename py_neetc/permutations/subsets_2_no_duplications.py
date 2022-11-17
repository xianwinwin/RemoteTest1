from datetime import datetime

class Solution:

    def subsetsWithDup(self, nums):
        
        res = []  
        nums.sort()

        def dfs(index, combo):
            if index==len(nums):                
                if combo not in res:
                    res.append(combo[:])
                return
            
            combo.append(nums[index])
            dfs(index+1,combo)
            combo.pop()
            dfs(index+1,combo)

        dfs(0,[])
        return res
        
        
if __name__=='__main__':
    print ("Start...")    
    start = datetime.now()

    s = Solution()

    nums = [1,2,2]
    sets = s.subsetsWithDup(nums)  
    for s in sets:
        print (s)
    print("len:=",len(sets))

    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)

    print ("ENDx")
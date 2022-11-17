from datetime import datetime

class Solution:

    def subsetsWithDup(self, nums):
        
        res = []  
        nums.sort()

        def dfs(index, combo):
            if index==len(nums):
                res.append(combo[:])
                return
            
            combo.append(nums[index])
            dfs(index+1,combo)
            combo.pop()

            #check that the next number is not the same
            while index<len(nums)-1 and nums[index+1]==nums[index]:
                index +=1

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

    print ("END")


'''
    #check this version, mroe efficient - looks at the index and iterate upwards to see if there are duplicates
    def subsetsWithDup(self, nums):
        
        res = []  
        nums.sort()

        def dfs(index, combo):
            if index==len(nums):
                res.append(combo[:])
                return
            
            combo.append(nums[index])
            dfs(index+1,combo)
            combo.pop()

            #check that the next number is not the same
            while index<len(nums)-1 and nums[index+1]==nums[index]:
                index +=1

            dfs(index+1,combo)

        dfs(0,[])
        return res

'''


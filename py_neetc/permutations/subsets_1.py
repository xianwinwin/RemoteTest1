'''
https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all possible 
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

https://www.youtube.com/watch?v=REOH22Xwdkk
Subsets - Backtracking - Leetcode 78

Note: the order is NOT important:
['a', 'b', 'c', 'd'] = ['a', 'b', 'd', 'c']
we're only liiking for the subsets:
['a', 'b', 'c', 'd']
['a', 'b', 'c']
so you don't have to ask if the item is in (like in permutation)
'''


from datetime import datetime

class Solution:

    def subsets(self, nums):
        
        res = []        
        def dfs(index,combo):
            if index==len(nums): #stop case when the index has arrived to the end of the nums [1,2,3] (len=3)
                res.append(combo[:])
                return
                                
            combo.append(nums[index]) #add item (say X)
            dfs(index+1,combo)
            combo.pop() #do not include item X
            dfs(index+1,combo) #note combo DOESNT have X 

        dfs(0,[])
        return res
        
        
if __name__=='__main__':
    print ("Start...")    
    start = datetime.now()

    s = Solution()

    nums = ['a','b','c','d']
    sets = s.subsets(nums)  
    for s in sets:
        print (s)
    print("len:=",len(sets))

    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)

    print ("END!")
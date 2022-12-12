#https://leetcode.com/problems/combination-sum-ii/
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''
from utilities import MyUtilities
from collections import defaultdict

class Solution:

    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(index, combo): 
            sum_combo =  sum(combo)
            if sum_combo==target:
                res.append(sorted(combo[:]))
                return
            else:
                if sum_combo>target:
                    return
            
            prev = -1 # optimization! 
                      # if the next item is just like the previous 
                      # - no need to check it after you popped it! 
            for i in range(index, len(candidates)):
                if prev==candidates[i]:
                    continue

                combo.append(candidates[i])
                dfs(i+1, combo)
                combo.pop()
                prev = candidates[i]

        dfs(0, [])
        return res


if __name__=='__main__':
    print ("Start...x")
 
    n = [10,1,2,7,6,1,5]
    target = 8 

    s = Solution()
    v = s.combinationSum2(n, target)  
    print ("v:=",v)
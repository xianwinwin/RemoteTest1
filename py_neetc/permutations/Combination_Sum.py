'''
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

'''

from datetime import datetime

class Solution:

    def combinationSum(self, candidates, target):

        res = set()

        def dfs(combo):            
            total = sum(combo)
            if total==target:
                res.add(tuple(sorted(combo[:])))
                return
                            
            if total>target:
                return
            
            for e in candidates: #note, you can send an index here instead of iterations BUT you'll have 2 dfs()
                combo.append(e)
                dfs(combo)
                combo.pop()

        dfs([])
        return [list(sl) for sl in res]
        
        
if __name__=='__main__':
    print ("Start...")    
    start = datetime.now()

    s = Solution()

    candidates  = [2,3,6,7]
    target = 7 
    res = s.combinationSum(candidates, target)  
    for r in res:
        print (r)

    print ("END")
 
'''
https://leetcode.com/problems/count-numbers-with-unique-digits/
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
excluding 11,22,33,44,55,66,77,88,99

'''

from datetime import datetime

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n==0:
            return 1
        if n==1:
            return 10

        #get all non unique combos:
        res = []
        def dfs(combo):
            if len(combo)==n:
                res.append(combo[:])
                return
        
            for i in range (0,10):
                if i not in combo or (combo and combo[0]==0) :
                    combo.append(i)
                    dfs(combo)
                    combo.pop()

        dfs([]) 

        for i,e in enumerate(res):
            print (i,e)
        return len(res)+1

if __name__=='__main__':
    print ("Start...")
    start = datetime.now()

    s = Solution()
    n=3
    counter = s.countNumbersWithUniqueDigits(n) 
     
    print ('len:=',counter)
    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)
    print ("END!")
'''
https://leetcode.com/problems/daily-temperatures/
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''


class Solution:
 
    def dailyTemperatures(self, temperatures):
 
        res = [0]*len(temperatures)
        stack = [] # tuple (temp, index)    <---- this is the trick: SAVE THE INDEX    
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                _ , index = stack.pop() 
                res[index] = i - index # how many days from i to index
            stack.append( (t,i) )

        return res

if __name__=='__main__':
    print ("start...")

    temperatures = [73,74,75,71,69,72,76,73]
    s = Solution()
    res  = s.dailyTemperatures(temperatures)
    print ("res:=",res)

    print ("END!")
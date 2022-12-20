#https://leetcode.com/problems/game-of-life/

class Solution:
 
    def dailyTemperatures(self, temperatures):
 
        res = [0]*len(temperatures)
        stack = [] # tuple (temp, index)        
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack_tuple = stack.pop()
                #stack_temp  = stack_tuple[0]
                stack_index = stack_tuple[1]
                res[stack_index] = i - stack_index
            stack.append( (t,i) )

        return res

if __name__=='__main__':
    print ("start...")

    temperatures = [73,74,75,71,69,72,76,73]
    s = Solution()
    res  = s.dailyTemperatures(temperatures)
    print ("res:=",res)

    print ("END!")
#https://leetcode.com/problems/valid-parentheses/
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''

class Solution:
 
    def isValid(self, s: str) -> bool:


        close_open = {')':'(',']':'[','}':'{'} #K=close, V=open
        stack = []
        for c in s:            
            if not close_open.get(c,None): #if this is OPEN parenthasis - add it
                stack.append(c)
            elif not stack:
                return False
            else:
                open_value = close_open[c] #'}'
                stack_value = stack.pop()
                if open_value!=stack_value:
                    return False

        return True if not stack else False

if __name__=='__main__':
    print ("start...")

    input = '[([])()[]{]}]'
    s = Solution()
    valid  = s.isValid(input) #[([])()[]{]}]
    print ("valid:=",valid)

    print ("END!")
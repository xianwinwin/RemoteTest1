'''
https://leetcode.com/problems/generate-parentheses/
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

class Solution:

    def generateParenthesis(self, n: int):

        res = []
        d = {'open':0,'close':0}
        def dfs(combo):
            if len(combo)==n*2:
                res.append(''.join(combo))
                return
            
            for e in ['(',')']:

                #check validity: open must be equal or higher than close
                id_valid = False
                if e=='(':
                    if d['open']+1<=n and d['open']+1 - d['close']>=0:
                        id_valid=True
                        d['open']=d['open']+1
                else:
                    if d['close']+1<=n and d['close']+1<=d['open']:
                        id_valid=True
                        d['close']=d['close']+1

                if id_valid:
                    combo.append(e)
                    dfs(combo)
                    p = combo.pop()
                    if p=='(':
                        d['open']=d['open']-1
                    else:
                        d['close']=d['close']-1

        dfs([])
        return res
            

if __name__=='__main__':
    print ('start...')

    str = 'abcabcbb'
    s = Solution()
    n=3
    res = s.generateParenthesis(n)
    for i, r in enumerate(res):
        print (i,r)
    print (res)
    print ("END ")
 
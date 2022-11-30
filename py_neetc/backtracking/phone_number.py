#https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

class Solution:

    def letterCombinations(self, digits):

        if not digits:
            return []
 
        digit2char = {'1': '', '2': 'abc', '3': 'def',
                      '4': 'ghi',  '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}
        res = []

        def dfs(index, combo):
 
            if len(combo)==len(digits):
                res.append(''.join(combo[:]))
                return

            digit = digits[index]
            chars = digit2char[digit]
            for c in chars:
                combo.append(c)
                dfs(index+1,combo)
                combo.pop()
                
        
        dfs(0,[])

        return res
        

if __name__=='__main__':
    print ("Start...")

    digits = "22233"
    s = Solution()
    res = s.letterCombinations(digits) 
    print (res)

    print ("END!")
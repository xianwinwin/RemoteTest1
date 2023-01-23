'''
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

'''

class Solution:

    def countAndSay(self, n: int) -> str:
        
        def say(s):
            my_str = ''
            l, r = 0, 0
            key = s[r]
            freq = 0
            while l<=r and l<len(s):
                while l<len(s) and r<len(s) and s[r]==key:
                    freq+=1
                    r+=1
                my_str+=str(freq)+key
                l=r
                freq=0
                key=s[r] if r<len(s) else None

            return my_str

        def dfs(n):
            if n==1:
                return '1'

            v = dfs(n-1)
            return say(v)

        return dfs(n)
        

        
if __name__=='__main__':
    print ('start...')
    
    n=3
    s = Solution()
    res = s.countAndSay(n)
    print (res)
    print ("END ")
 
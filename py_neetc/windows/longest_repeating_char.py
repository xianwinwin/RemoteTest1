'''
https://leetcode.com/problems/longest-repeating-character-replacement/
You are given a string s and an integer k. You can choose any character of the string and change it to 
any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

'''

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
 
        cache = {}
        max_repetition = 0 
        r=0

        def cache_ok():
            max_value = 0
            total = 0
            for _,value in cache.items():
                max_value = max(max_value, value)
                total+=value

            total = total - max_value
            return total-k <=0
            
            
        for l in range(0,len(s)):
            while l<=r and r<len(s):    
                print ('L:=',l,'R:=',r,' V:=',s[r])   
                cache[s[r]] = cache.get(s[r],0)+1
                #check if valid 
                if cache_ok():
                    r+=1
                    max_repetition = max (r-l,max_repetition)
                else:
                    cache[s[l]] = cache.get(s[l],0)-1
                    r+=1
                    break
        
        return max_repetition
        

        
if __name__=='__main__':
    print ('start...')
    
    s = "AAAA"
    k = 0

    solution = Solution()
    res = solution.characterReplacement(s,k)
    print (res)
    print ("END ")
 
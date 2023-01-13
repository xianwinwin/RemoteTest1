'''
https://leetcode.com/problems/longest-repeating-character-replacement/
Longest Repeating Character Replacement - Leetcode 424 - Python

You are given a string s and an integer k. You can choose any character of the string and change 
it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4

accepted!
'''

import heapq


class Solution:
 
    def characterReplacement(self, s: str, k: int):

        l,r = 0,1
        res=0  
        cache = {}
        for c in s:            
            cache[c]=0
 
        def cache_sum(remove_max=True):
            
            max_char = 0
            total = 0
            for _,v in cache.items():
                total+=v
                max_char = max(v,max_char)
            
            if remove_max:
                return total-max_char
            return total
        
        for my_char in s:
            cache[my_char] = cache[my_char]+1
            if cache_sum()>k: #not good move window from the left one click right and remove the item
                cache[s[l]] = cache[s[l]]-1
                l=l+1                
            else:
                #OK - add the item to the window & move right                
                res = max(res, cache_sum(remove_max=False))
                r+=1                                
            
        return res

if __name__=='__main__':
    print ("start...")

    s = "ABAB"
    k = 2
    solution = Solution()
    res  = solution.characterReplacement(s,k)
    print ("res:=",res)

    print ("END!")
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0

        l_ptr = 0
        r_ptr = 0  
        my_set = set()
        while r_ptr<len(s):
            
            c = s[r_ptr]            
            if c not in my_set:
                my_set.add(c)
                r_ptr+=1
            else:
                my_set.remove(s[l_ptr])
                l_ptr+=1
                
            max_length = max(len(my_set),max_length)
        
        return max_length
            

if __name__=='__main__':
    print ('start...')

    str = 'abcabcbbacser'
    s = Solution()
    res = s.lengthOfLongestSubstring(str)
    print (res)
    print ("END ")
 
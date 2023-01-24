'''
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

''' 

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        #s2 big; s1 = small        
        l,r=0,len(s1)-1
        
        s1_cache = {}
        for c in s1:
            s1_cache[c] = s1_cache.get(c,0)+1

        window_cache = {}
        for i in range(0,len(s1)):
            c = s2[i]
            window_cache[c] = window_cache.get(c,0)+1

        def cache_check():
            for wk,wv in window_cache.items():
                s1_v = s1_cache.get(wk,None)
                if not s1_v:
                    return False
                if s1_v!=wv:
                    return False
            return True

        round_one = True
        while r>l and r<len(s2):
            
            if round_one:
                round_one = False
            else:        
                #add new item        
                right_char = s2[r]
                window_cache[right_char]=window_cache.get(right_char,0)+1
 
            window_str = s2[l:r]
            if cache_check():
                return True
            
            left_char = window_str[0] 
            window_cache[left_char]=window_cache[left_char]-1
 
            r+=1
            l+=1
        
        return False
 

if __name__=='__main__':
    print ("start...")
    
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()     
    r = s.checkInclusion(s1,s2)
    print ("r:=",r)

    print ("END!")
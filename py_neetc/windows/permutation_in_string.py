'''
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

''' 

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        #s2 big; s1 = small        
        r = len(s1)-1
        
        s1_cache = {}
        for c in s1:
            s1_cache[c] = s1_cache.get(c,0)+1

        def cache_check():
            for s1k,s1v in s1_cache.items():
                wv = window_dict.get(s1k,None)
                if not wv:
                    return False
                if wv!=s1v:
                    return False
            return True


        #initial window
        window_dict = {}
        window = s2[0:len(s1)]
        for w in window:
            window_dict[w] = window_dict.get(w,0)+1

        if cache_check():
            return True

        for i in range(1, len(s2)):
            w = s2[i]
            #remove tail and add new char
            tail = window[0]
            window_dict[tail] = window_dict[tail]-1

            #add new
            window_dict[w] = window_dict.get(w,0)+1
            
            #new window
            window = window[1:]+w

            #check
            if cache_check():
                return True
        
        return False
 

if __name__=='__main__':
    print ("start...")
    
    s1 = "ooa"
    s2 = "eidbaooo"
    s = Solution()     
    r = s.checkInclusion(s1,s2)
    print ("r:=",r)

    print ("END!")
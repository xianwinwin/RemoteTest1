'''
https://leetcode.com/problems/string-matching-in-an-array/

Given an array of string words, return all strings in words that is a substring of 
another word. You can return the answer in any order. A substring is a contiguous sequence of characters within a string

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
'''

class Solution:
    def stringMatching(self, words):
        #sort by length of word
        words.sort(key=lambda x: len(x))

        res = set()

        for ptr_w in range(0,len(words)-1):
            for w in range (ptr_w+1, len(words)):
                subw = words[ptr_w]
                word = words[w]
                if subw in word:
                    res.add(subw)

        return list(res)


if __name__=='__main__':
    print ("Start")
 

    s = Solution()
    words = ["mass","as","hero","superhero"]
    res = s.stringMatching(words)
    print ("\nRes:= ",res)
    
    print ("END")
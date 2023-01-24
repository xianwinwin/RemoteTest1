'''
['d', 'a', 'c', 'b']
['d', 'b', 'a', 'c']
['d', 'b', 'c', 'a']
['d', 'c', 'a', 'b']
['d', 'c', 'b', 'a']

'''
class Solution:

    def rearrange(self, word):

        res = []
        def dfs(combo):
            if len(combo)==len(word):
                res.append(combo[:])
                return 
            
            for c in word:
                if c not in combo:
                    combo.append(c)
                    dfs(combo)
                    combo.pop()
             
        dfs([])
        return res
        
 
if __name__=='__main__':
    print ("Start...") 

    s = Solution()  
    word = 'abcd'
    perms = s.rearrange(word) 
    
    for p in perms:
        print (p)
    print ("END!")

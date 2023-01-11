from datetime import datetime
#https://leetcode.com/problems/combinations/submissions/

class Solution:

    def combine(self, n,k):

        res = []
        def dfs(index, combo):
            if len(combo)==k:
                res.append(combo[:])
                return

            for i in range(index,n+1): 
                combo.append(i)
                dfs(i+1,combo)
                combo.pop()
                
        dfs(0, [])
        return res
        
 
if __name__=='__main__':
    print ("Start...")
    start = datetime.now()

    s = Solution()

    n = 5
    k = 2
    perms = s.combine(n,k) 
    
    for p in perms:
        print (p)

    #[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print ('len:=',len(perms))
    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)
    print ("END!")
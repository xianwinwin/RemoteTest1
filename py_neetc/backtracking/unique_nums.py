from datetime import datetime

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        #get all non unique combos:
        res = []
        def dfs(combo):
            if len(combo)==n:
                res.append(combo[:])
                return
            
        
            if i not in combo:
                combo.append(i)
                dfs(combo)
                combo.pop()
                combo.append(i)

        dfs([]) 
 
        for i,e in enumerate(res):
            print (i,e)
            if i>15:
                break

        added = 10 
        return len(res)+1

if __name__=='__main__':
    print ("Start...")
    start = datetime.now()

    s = Solution()
    n=3
    counter = s.countNumbersWithUniqueDigits(n) 
     
    print ('len:=',counter)
    exec_time = (datetime.now()-start).total_seconds()
    print ("exec time sec :=",exec_time)
    print ("END!")
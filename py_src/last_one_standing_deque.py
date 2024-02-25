from datetime import datetime
from collections import deque

class Solution:
    
    def magic_deque(self, n, k):
        
        q = []
        dq = deque(n)
        last_item = None
        while dq: 
            dq.rotate(-(k-1))
            last_item = dq.popleft()
            q.append(last_item)
 
        #print ('with deque',q)
        return last_item
        
    def magic_array(self, n, k):
        
        q = []
        last_item = None
        pointer = 0
        while n:
            pointer = (pointer+k-1) % len(n)
            v = n[pointer]
            last_item=v
            n.remove(v)
            q.append(v) 
                 
        print ('with array:',q)
        return last_item
  
  
if __name__=='__main__': 
    print ("Start")
    started = datetime.now()
    n1 = [3,6,4,9,12,13,16,18,21,88]
    #expected result: [4, 13, 21, 6, 16, 3, 18, 12, 88, 9]
    
    n2 = [3,6,4,9,12,13,16,18,21,88]
    
    n2=[i for i in range(0,50000)] #will not work with array!
    
    k = 3
    s = Solution()
    resA = s.magic_array(n1,k)
    resDQ = s.magic_deque(n2,k)
    print ('resA, last one standing:=',resA)
    print ('resDQ, last one standing:=',resDQ)
    
    exec_time = (datetime.now() - started).total_seconds()
    print (f"Ended in {exec_time} seconds")
ssh-add ~/.ssh/id_rsa ssh-add ~/.ssh/git_mac_uws
'''
 n = [ ,6, , , , , ,18, , ]
 
'''
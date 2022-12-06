import heapq
from collections import Counter

class Solution:

    def reorganizeString(self, s: str) -> str:
        
        d = Counter(list(s))
        
        hq = [(-v, k) for k, v in d.items()]                
        heapq.heapify(hq)
        
        res = []
        counter = len(s)
        while counter>0:
            my_tuple = heapq.heappop(hq) # tuple (most frequent, char)
            freq = my_tuple[0]
            char = my_tuple[1]
                        
            if len(res)>0:
                prev_value = res[-1]
                if char ==prev_value:
                    if not hq:
                        return ''
                    nxt_tuple = heapq.heappop(hq) # tuple (most frequent, char)
                    heapq.heappush(hq,my_tuple) #return original the tuple back to heapq
                    freq = nxt_tuple[0]
                    char = nxt_tuple[1]

            res.append(char)
            if freq+1<0:                 
                heapq.heappush(hq,(freq+1, char)) # tuple (msot frequent, char)

            counter-=1
        
        return ''.join(res)
        

if __name__=='__main__':
    print ('start...')

    #my_str = "aaabqqqqieudjjjjdusydjjj"
    my_str = "baaba"
    s = Solution() 
    r = s.reorganizeString(my_str)
    print ('r:=',r)

    print ("END ")
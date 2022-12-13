#https://www.youtube.com/watch?v=obWXjtg0L64&t=83s
#Time Complexity of Bellman Ford algorithm is relatively high O ( V ⋅ E ) , in case E = V 2 , O ( V 3 ) .
import heapq
from collections import defaultdict 


class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k) -> int:

        #adjeceny list
        terminals = set()
        for start, to, _ in flights:           
            terminals.add(start)
            terminals.add(to)

        prices = {}
        for t in terminals:
            prices[t]=float('inf')
        prices[src]=0

        for i in range(0,k+1):
            temp_prices = prices.copy()
            for s,t,p in flights: #s=start,t=to,p=price
                if prices[s]==float("inf"):
                    continue
                if prices[s]+p < temp_prices[t]:
                    temp_prices[t] = prices[s]+p
            
            prices = temp_prices

        if not prices.get(dst,None) or prices.get(dst)==float('inf'):
            return -1         

        return prices[dst]
        
if __name__=='__main__':
    print ("Start...")
     
    s = Solution()

    flights = [ ['A','B',1],['B','C',3.1],['C','E',0.8],['C','D',2.1],['D','G',1.1],['C','F',2.1],
    ['B','F',4],['B','J',0.6],['Q','J',0.5],['A','Q',0.8],['A','M',2],['M','N',4.2],['B','H',3],
    ['H','Z',0.45],['Z','D',5],['A','H',2],['Z','F',0.8]]

    src = "A"
    dst = 'B'
    n = 2
    k = 20

    cost = s.findCheapestPrice(n, flights, src, dst, k)
    print ('cost:=',cost)

    print ("END")
    
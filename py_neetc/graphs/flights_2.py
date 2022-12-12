#https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city to i 
with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst 
with at most k stops. If there is no such route, return -1.
'''

import heapq
from collections import deque, defaultdict

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k):
        
        adj = defaultdict(list) #K=From, V = [(weight, to), (weight, to)...]
        for f,t,w in flights: #f=from, t=to, w=weight
            adj[f].append( (w,t,[]) )

        hq = []
        for i in adj[src]:
            hq.append (i)
        
        ft={}
        origin = None
        heapq.heapify(hq) 
        while hq:

            weight, to, arry = heapq.heappop(hq)
            print ("to",to, 'weight',weight, '-->',arry)

            if to==dst: 
                return weight
            
            for w,t, ary in adj[to]:
                w+=weight
                ary.append( ('from',to,'to',t) )
                
                heapq.heappush(hq, (w,t, ary) )
        
        return -1
        

if __name__=='__main__':
    print ("Start...")
  
    flights = [[0,3,3.2],[3,4,3.1],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    n = 11
    src = 0
    dst =2
    k =2

    s = Solution()
    price = s.findCheapestPrice(n,flights,src,dst,k)
    print ('price:=',price)

    print ("END")
    
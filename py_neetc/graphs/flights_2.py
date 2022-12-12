#https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city to i 
with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst 
with at most k stops. If there is no such route, return -1.

So overall time complexity is O(E+V)*O(LogV) which is O((E+V)*LogV) = O(ELogV) 
'''

import heapq
from collections import deque, defaultdict

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k):
        
        adj = defaultdict(list) #K=From, V = [(weight, to), (weight, to)...]
        for f,t,w in flights: #f=from, t=to, w=weight, comming_from
            adj[f].append( (w,t,f) )

        hq = []
        for i in adj[src]:
            hq.append (i)
        heapq.heapify(hq) 

        routes = []
        while hq:
            weight, to, cf = heapq.heappop(hq)
            print (cf,"-->",to) 
            routes.append( (cf,to) )

            if to==dst:  
                print (routes) #use dikstra_routes_dfs to find the path from src to dst
                return weight
            
            for w,t, cf in adj[to]: 
                w+=weight                 
                heapq.heappush(hq, (w,t, to) )
        
        return -1
        

if __name__=='__main__':
    print ("Start...")
  
    flights = [[0,3,3.2],[3,4,3.1],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[9,4,0.5],[1,10,1],[10,2,1],[1,2,100]]
    n = 11
    src = 0
    dst =2
    k =2

    s = Solution()
    price = s.findCheapestPrice(n,flights,src,dst,k)
    print ('price:=',price)

    print ("END")
    
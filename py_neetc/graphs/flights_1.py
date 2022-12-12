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
                
        adj = defaultdict(list)
        for f in flights:
            start = f[0]
            finish = f[1]
            price = f[2]
            adj[start].append((price,finish,0)) 
 
        #[5]:[($41,7,0),($21,7,0)] postfix 0 is the time to get there 

        hq = [] #holds tuples [(price,name,#of_connections),(price,name,#of_connections)...]
        for nei in adj[src]:
            hq.append( (nei[0],nei[1], nei[2]) )  #
        
        heapq.heapify(hq)
        visited = set()
        
        res = []
        while hq:

            item = heapq.heappop(hq)
            price = item[0]
            name = item[1]     
            connections = item[2] 

            if connections-1>k:
                continue    

            if item in visited:
                continue
            
            visited.add(name)

            if name==dst:
                res.append( (connections, price) )
                continue

            for nei in adj[name]:
                if nei[1] not in visited:
                    heapq.heappush(hq, (nei[0] + price, nei[1], nei[2] + connections) )
        
        if res:
            return heapq.heappop(res)[1]
        return -1
        

if __name__=='__main__':
    print ("Start...")
 
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0 
    dst = 3
    k = 1

    flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    n = 11
    src = 0
    dst =2
    k =2


    s = Solution()
    price = s.findCheapestPrice(n,flights,src,dst,k)
    print ('price:=',price)

    print ("END")
    
import heapq
from collections import defaultdict 


class Solution:

    def findCheapestPrice(self, n, flights, src, dst, k=0) -> int:
        
        src_prices = {} #K = to , V= price
        adj = defaultdict(list)
        for f in flights:
            frm   = f[0]
            to    = f[1]
            price = f[2]            
            adj[frm].append( (price,to) )
            if frm==src:
                src_prices[to]=price
            else:
                src_prices[to]=float("inf")
        
        for i in range(0,k+1):
            
            for nei in adj[]
                        

        return []
        
if __name__=='__main__':
    print ("Start...")
     
    s = Solution()

    flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    src = 0
    dst = 2
    n = 11


    cost = s.findCheapestPrice(n, flights, src, dst)
    print ('cost:=',cost)

    print ("END")
    
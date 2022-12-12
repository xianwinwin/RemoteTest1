import heapq
from collections import deque, defaultdict
import heapq

'''
    Key items: 
    1. build adjacent list
    2. add to heapq the neighbors (from src)
    3. iterate from current heapq and always work on the whats the minimum 
    3. favor the minimum IF not visited already!  

    Note: remember to upgrade the weight each time you work on an edge
'''

class Solution:

    def shortes_path(self, graph, src, dst):
        
        adj = defaultdict(list) #K=edge, V= [ (weight,dest), (weight,dest)... ]
        for g in graph:
            frm = g[0]
            to = g[1]
            weight = g[2]
            adj[frm].append( (weight,to) ) 
            adj[to].append( (weight,frm) ) #bidirectional 

        hq = []
        for i in adj[src]:
            hq.append( i )

        heapq.heapify(hq)
        visited = set(src)

        while hq:
            item = heapq.heappop(hq) #item (weight,to)
            weight = item[0]
            to = item[1]

            if to in visited:
                continue
                
            visited.add(to)
            
            if to==dst:
                return weight

            for nei in adj[to]:
                if nei[1] not in visited:
                    heapq.heappush(hq, (nei[0]+weight,nei[1]) )
            
            
        return -1
        

if __name__=='__main__':
    print ("Start...")
   
    s = Solution()

    graph = [('A','B',6),('A','D',1),('D','B',1.2),('B','E',2.1),('D','E',1),('E','C',5),('B','C',4)]
    src = 'A'
    dst = 'C'

    price = s.shortes_path(graph, src, dst)
    print ('price:=',price)

    print ("END")
    
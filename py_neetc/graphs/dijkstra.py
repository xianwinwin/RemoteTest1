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

    def shortest_path(self, graph, src, dst):
        
        adj = defaultdict(list) #K=edge, V= [ (weight,dest), (weight,dest)... ]
        for frm, to, weight in graph:
            adj[frm].append( (weight,to) ) 
            adj[to].append( (weight,frm) ) #bidirectional 

        hq = []
        for i in adj[src]:
            hq.append( i )

        heapq.heapify(hq)
        visited = set(src)
        
        while hq:
            weight, to = heapq.heappop(hq) #item (weight,to)

            if to in visited:
                continue
                
            visited.add(to)            

            if to==dst:
                return weight

            for neiw, nei in adj[to]:
                if nei not in visited:
                    heapq.heappush(hq, (neiw+weight,nei) ) #note: adding weight
                        
        return -1 #didnt find anything 
        

if __name__=='__main__':
    print ("Start...")
   
    s = Solution()

    graph = [('A','B',6),('A','D',1),('D','B',1.2),('B','E',2.1),('D','E',1),('E','C',5),('B','C',4)]
    src = 'A'
    dst = 'C'

    price = s.shortest_path(graph, src, dst)
    print ('price:=',price)

    print ("END")
    
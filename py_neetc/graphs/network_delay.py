import heapq
from collections import defaultdict

#https://leetcode.com/problems/network-delay-time/
#using Dijkstra's algorithm 

class Solution:

    def networkDelayTime(self, times, n: int, k: int) -> int:

        #k= start node
        #n = number of nodes

        adj = defaultdict(list) #{K=start; V=[(To, price), (To, price)]}                
        for t in times:
            start = t[0]
            to = t[1]
            weight = t[2]
            adj[start].append((weight,to))  

        hq = []
        for nei in adj[k]:
            hq.append(nei)
        
        heapq.heapify(hq)

        t = 0
        visited = set()
        visited.add(k)

        while hq: 

            item = heapq.heappop(hq)
            node_name = item[1]
            if node_name in visited:
                continue

            node_weight = item[0]
            t = max(t, node_weight)
            visited.add(node_name)

            for nei in adj[node_name]:
                if nei[1] not in visited:
                    heapq.heappush(hq,(nei[0]+node_weight,nei[1])) #note we're pushing the ndoe_weight from the previous result!!!
                  
        return t if len(visited)==n else -1

if __name__=='__main__':
    print ("Start...")
    
    
    times = [[2,1,1],[2,3,1],[3,4,1]]    
    n = 4
    k = 2
    
    '''
    times = [[1,2,1],[2,3,2],[1,3,2]]
    n=3
    k=1
    

    times = [[1,2,1],[2,3,2],[1,3,4]]
    n=3
    k=1
    '''

    s = Solution()
    timne_taken = s.networkDelayTime(times, n, k)
    print ('time_taken:=',timne_taken)

    print ("END")
    
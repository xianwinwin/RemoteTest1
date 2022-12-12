import heapq
from collections import defaultdict
#https://leetcode.com/problems/min-cost-to-connect-all-points/

'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''

#Prim's algorithm has a time complexity of O(V2), V being the number of vertices and can be improved up to O(E log V) using Fibonacci heaps
#Why V^2? note how it works: it will 'hook' each point to ALL points (note 2 for loops of assoication)

class Solution:

    def minCostConnectPoints(self, points) -> int:

        def get_manhattan_distance(p0,p1):
            x1, y1 = p0[0], p0[1]
            x2, y2 = p1[0], p1[1]

            return abs(x1-x2) + abs(y1-y2)

        #build adjacent list: {K=from_point, to=[ (dist, to_point) ] }
        #need to calculate the distance FROM each Point to the OTHER (hence time complexity is: O(V^2) )
        adj = defaultdict(list)
        N = len(points)
        for i in range (0,N):
            p0 = points[i]
            for j in range(i+1,N):
                p1 = points[j]
                dist = get_manhattan_distance(p0,p1)
                adj[ tuple(p0) ].append( (dist, tuple(p1) ) )
                adj[ tuple(p1) ].append( (dist, tuple(p0) ) )
            
        #use minheap to connect the next point
        min_heap = [ (0, tuple(points[0])) ] #get any point (you can start with the first one)
        visited = set()
        res = 0 
        while min_heap:
            dist, my_point = heapq.heappop(min_heap)             
            #did we visit this point before? 
            if my_point in visited:
                continue
            visited.add(my_point)
            res +=dist

            #add all neighbors to min_heap
            for nei in adj[my_point]:
                if nei[1] not in visited:
                    heapq.heappush(min_heap,nei) 
        return res
        
if __name__=='__main__':
    print ("Start...")
     
    s = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    cost = s.minCostConnectPoints(points)
    print ('cost:=',cost)

    print ("END")
    
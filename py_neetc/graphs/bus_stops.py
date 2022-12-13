#https://leetcode.com/problems/bus-routes/
'''
You are given an array routes representing bus routes where routes[i] is a bus route 
that the ith bus repeats forever.
For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the 
sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you 
want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. 
Return -1 if it is not possible.
'''

# incorrect result - may need to use dijkstra 

from collections import defaultdict
from collections import deque

class Solution:

    def numBusesToDestination(self, routes, source, target):
        
        graph = defaultdict(list) #from --> [to]
        buses = {} # set the bus belongs to
        ROWS = len(routes)        

        #create the graph
        set_counter = 0
        for r in range(0,ROWS):
            COLS = len(routes[r])
            set_counter+=1
            for c in range(0,COLS):
                bus_from = routes[r][c]
                bus_to  = routes[r][c+1] if c+1<COLS else routes[r][0]
                graph[bus_from].append(bus_to)  
                buses[bus_from] = set_counter

        visited = set()
        d = deque()
        d.append(source)
        visited_line = set()

        while d:
            source = d.popleft()
            if source==target:
                return len(visited)

            visited_line.add(source)

            bus_id = buses[source] 
            visited.add(bus_id)

            destinations = graph[source]
            for des in destinations:
                if des not in visited_line:
                    d.append(des)                    

        return -1


if __name__=='__main__':
    print ("start")

    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6

    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
     
    routes = [[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]
    source = 20
    target = 8

    routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
    source = 37
    target = 28

    s = Solution()
    num_buses = s.numBusesToDestination(routes,source,target)
    print ('num_buses',num_buses)

    print ("EnND")
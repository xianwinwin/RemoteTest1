#https://leetcode.com/problems/clone-graph/
#133. Clone Graph
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        return str(self.val)+' --> # neis:='+str(len(self.neighbors))
        

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node': 
        if not node:
            return None

        graph = {}
        dq = deque() 
        dq.append( node )  

        while dq: 
            original_node = dq.popleft()

            cloned_node = graph.get(original_node, None)
            if not cloned_node:
                cloned_node = Node(original_node.val)
                graph[original_node]=cloned_node            
                               
            for nei in original_node.neighbors:                
                cloned_nei = graph.get(nei,None)
                if not cloned_nei:
                    cloned_nei = Node(nei.val)
                    graph[nei]=cloned_nei
                    dq.append(nei)

                cloned_node.neighbors.append(cloned_nei)
 
        return graph[node]



if __name__=='__main__':

    print("start...")
    adj_list = [[2,4],[1,3],[2,4],[1,3]]
    cached = {}
    ptr = None
    for i, values in enumerate(adj_list):
        num = i+1
        n = cached.get(num,None)
        if not n:            
            n = Node(i+1)
            cached[num]=n

        for v in values:
            vn = cached.get(v,None)
            if not vn:
                vn = Node(v)
                cached[v]=vn
            n.neighbors.append(vn)

        if not ptr:
            ptr = n
 
    s = Solution()    
    cloned = s.cloneGraph(ptr)    
    print (cloned)
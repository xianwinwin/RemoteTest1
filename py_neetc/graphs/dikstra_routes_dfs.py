'''
    with this none circulating path - we can use DFS() to get the route from src to target 
'''

import heapq
from collections import deque, defaultdict

class Node:
    def __init__(self, val, nei=None):
        self.val = val
        self.nei = []
    
    def append_nei(self, node):
        self.nei.append(node)

class Solution:

    def find_route(self, routes, src, tgt):

        d = {}
        for r in routes:
            val = r[0]
            nei_val = r[1]
            
            v_node = d.get(val,None)
            if not v_node:
                v_node = Node(val)
                d[val]=v_node
            
            nei = d.get(nei_val,None)
            if not nei:
                nei_node = Node(nei_val)
                d[nei_val]=nei_node
                
            v_node.append_nei(nei_node)


        def dfs(node, combo):
            if not node:
                return

            if node.val==tgt:
                res.append(combo[:])
                return

            for nei in node.nei:
                combo.append(nei.val)
                dfs(nei, combo)
                combo.pop()

        res = []
        dfs(d[src], [d[src].val] )
        print (res)

        return -1
        

if __name__=='__main__':
    print ("Start...")
  
    routes = [(0,6),(0,3),(0,5),(0,7),(7,8),(8,9),(9,4),(9,1),(1,10),(10,2)]
    src = 0
    tgt = 2

    s = Solution()
    levels = s.find_route(routes, src, tgt)
    print ('levels:=',levels)

    print ("END")
    
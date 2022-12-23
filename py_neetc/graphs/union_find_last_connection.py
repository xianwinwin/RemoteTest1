#https://leetcode.com/problems/redundant-connection/
#Redundant Connection - Union Find - Leetcode 684 - Python
#over simplicti version - for REAL union find you should use a DFS for find()
'''
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one 
additional edge added. The added edge has two different vertices chosen from 1 to n, 
and was not an edge that already existed. The graph is represented as an array edges of 
length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi 
in the graph. 
Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.
'''

#note: this is an over simplification of Union-Find. Can be implemented properly with dfs()

from collections import defaultdict

class UnionFind:

    def findRedundantConnection(self, edges):

        def union(px,py):

            if px==py:
                return False

            values_x = graph.get(px,None)
            values_y = graph.get(py,None) 

            if (not values_x and not values_y) or (values_x and not values_y):
                graph[px].append(py)
            elif values_y and not values_x:
                graph[py].append(px)
            elif values_x and values_y: 
                del graph[py]
                graph[px].extend(values_y)
                graph[px].append(py)
            
            return True
        
        def find(item):
            #find the parent, if none exists - return the item as a parent
            if graph.get(item, None):
                return item

            for k,v in graph.items():
                if item in v:
                    return k
            
            return item

        graph = defaultdict(list)
        for e in edges:            
            x,y = e[0], e[1]    

            parent_x = find(x) 
            parent_y = find(y)

            f = union(parent_x, parent_y)
            if not f:
                return e


if __name__=='__main__':
    print("start...")

    edges =[[1,2],[2,3],[3,4],[1,4],[1,5]]#[[1,2],[1,3],[2,3]]    
    uf = UnionFind()
    e = uf.findRedundantConnection(edges)
    print ('e:=',e)
    
    print ("END")
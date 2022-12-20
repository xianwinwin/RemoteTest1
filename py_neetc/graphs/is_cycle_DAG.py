#Directed acyclic graph

'''
    Note: after you established the adjacent hast map you'll note 2 sets:
    visits and cycle. The cycle will hold all those dfs item per DFS iteration
    and will see if any course is in the cycle, if so - there's a cycle. 
    The visit, on the other hand will ensure that we dont churn the adjuscent list
    over and over. If you visited this c before - move to the next one. 
'''


from collections import defaultdict

class Solution:

    def is_cycle(self, edges):

        edges_set = set()
        adj = defaultdict(list) #K=course V=[ (pre-req-course, ()... ]
        for c,pr in edges:
            adj[c].append(pr)
            edges_set.add(c)
            edges_set.add(pr)
        
        cycle, visited = set(), set()
        def dfs(c):
            if c in cycle:
                return True
            
            if c in visited:
                return False

            prereqs = adj.get(c,None)
            if not prereqs:
                visited.add(c) 
                return False
            
            cycle.add(c)
             
            for p in prereqs:
                if dfs(p)==True:
                    return True
            cycle.remove(c) #important remove at the end knowing that there's no cycle and continue with the next one
            visited.add(c) #ok, visited - no need to visit again (also - must come at the end)

        for c in edges_set: 
            if dfs(c)==True:
                return True
            
        return False

if __name__=='__main__':
    print ('start...')

    edges = [[1,3],[1,0],[3,2],[3,5],[3,6],[0,8],[8,6],[6,4]]
    edges = [[3,1],[8,3],[1,8]]
    edges = [[0,1],[0,4],[0,2],[2,3],[1,3]] #https://www.scaler.com/topics/detect-cycle-in-directed-graph/
    s = Solution()
    f = s.is_cycle(edges) 
    print ("is cycle exists? :=",f)
    print ("end")
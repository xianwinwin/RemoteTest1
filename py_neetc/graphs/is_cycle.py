# graph valid leetcode 178 (preimum)
# https://www.youtube.com/watch?v=bXsUuownnoQ
# in order to find if there's a cycle, we'll make the adj hashTable and iterate over
# most importantly - send the previous value so you dont re-check it (see continue below) 
# check in the for loop (dj.keys()) if it is not visited 

# return True if Valid

from collections import defaultdict

class Solution:

    def is_valid(self, edges):

        #return True if valid, False if theres a circulation
        adj = defaultdict(list)
        
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        visited = set()
        def dfs(n, prev):
            if n in visited:
                return False
            
            visited.add(n)
            
            for nei in adj[n]: # no need to loop for None because it is bi-direction (it most be there)
                if nei==prev:
                    continue
                if dfs(nei,n)==False:
                    return False
        
        for i in adj.keys():
            if i not in visited:
                if dfs(i,-1)==False:
                    return False
        
        return True if len(adj.keys())==len(visited) else False

if __name__=='__main__':
    print ('start...')

    edges = [[1,0],[0,2],[0,3],[1,4]]
    s = Solution()
    f = s.is_valid(edges)
    print ("flag:=",f)
    print ("end")

#find number of connected components

class Solution:

    def countComponenets(self, n, edges):
 
        def dfs(e):
            if (e[0],e[1]) in visited:
                return
            
            visited.add((e[0],e[1]))
            #next edge?
            for nxt_e in edges:                
                if (nxt_e[0],nxt_e[1]) not in visited and (nxt_e[0]==e[1] or nxt_e[1]==e[0] or nxt_e[0]==e[0] or nxt_e[1]==e[1]) :
                    dfs(nxt_e)
        
        counter = 0
        cached = set()
        visited = set()
        edges.sort()
        for e in edges:
            if (e[0],e[1]) in cached:
                continue

            dfs(e)
            r = visited.intersection(cached)
            if not r:
                counter +=1
                cached.update(visited)

            visited = set()

        return counter



if __name__=='__main__':
    print ("Start...")

    edges = [[10,20],[20,30],[40,50],[45,50],[700,45],[30,700],[15,16],[2,3],[22,33]]
    n = 5
    s = Solution()
    counter = s.countComponenets(n,edges)
    print ('counter:=',counter)

    print ("END")
    
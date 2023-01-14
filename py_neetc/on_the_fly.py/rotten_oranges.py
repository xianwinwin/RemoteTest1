
import heapq
from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        
        visited = set()
        rottens = deque()
        ROWS, COLS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                g = grid[r][c]
                if g==2:
                   rottens.append( (r,c) )
                   visited.add( (r,c) )
        
        def bfs(x,y):

            #out of bound
            if x<0 or y<0 or x>=ROWS or y>=COLS:
                return 

            #processed already 
            if (x,y) in visited:
                return 
            
            #mark as rotten IF item is fresh
            if grid[x][y]==1:
                grid[x][y]=2
                rottens.append( (x,y) )
            visited.add( (x,y) )
            
        if not rottens:
            #is there one fresh?
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]==1:
                        return -1
            return 0

        #iteration
        t=-1
        while rottens: #as long as there are rottens
            len_rotten = len(rottens)
            for x in range(0, len_rotten): #current round
                r = rottens.popleft()
                x,y = r[0],r[1] #get coordinates to move to other adjacent cells
            
                for d in directions:
                    bfs(x+d[0], y+d[1])
            t+=1

        #is there one fresh left?
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
        return t


if __name__=='__main__':
    print ("start...")

    grid = [[2,1,1],[1,1,0],[0,1,1]]
    #grid = [[2,1,1],[0,1,1],[1,0,1]]

    s = Solution()
    r = s.orangesRotting(grid)
    print ('r:=',r)
    print ("END ")
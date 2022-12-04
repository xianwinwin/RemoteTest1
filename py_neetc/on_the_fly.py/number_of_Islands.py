
class Solution:
    def numIslands(self, grid) -> int:
         
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        res = [False]
        def dfs(r,c):
            if (r,c) in visited or r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]=='0':
                return 

            visited.add((r,c))
            if grid[r][c]=='1':
                res[0]=True
            
            directions = [ (r-1,c),(r+1,c),(r,c+1),(r,c-1) ]
            for dir in directions:                
                dfs(dir[0],dir[1])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1':
                    dfs(r,c)
                    if res[0]:
                        islands+=1
                    res[0]=False

        return islands
        

if __name__=='__main__':
    print ("Start...")

    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    s = Solution()
    num_islands = s.numIslands(grid) 
     
    print ('num_islands:=',num_islands)

    print ("END!")
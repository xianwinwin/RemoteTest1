'''
https://leetcode.com/problems/number-of-islands/description/
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    
    def numIslands(self, grid) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            #already visited?
            if  (r,c) in visited: 
                return 
            #out of bound?
            if r>=ROWS or c>=COLS or r<0 or c<0:
                return 
            
            #value is 0
            if grid[r][c]=='0':
                return

            visited.add((r,c)) #mark it so dont count again

            directions = [(r,c+1),(r,c-1),(r-1,c),(r+1,c)]
            for dir in directions:
                dr = dir[0]
                dc = dir[1]
                dfs(dr,dc)


        visited = set()
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1

        return islands
        

if __name__=='__main__':
    print ("Start...")

    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","1"],
        ["0","0","0","1","1"]
    ]

    s = Solution()
    num_islands = s.numIslands(grid) 
     
    print ('num_islands:=',num_islands)

    print ("END!")
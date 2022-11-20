

class Solution:

    def _get_neighbor_value(self, nr,nc):
        if nr<0 or nr>=len(board):
            return 0
        if nc<0 or nc>=len(board[0]):
            return 0
        
        symbol = board[nr][nc]
        if symbol==2 or symbol==3:
            return 0
        if symbol==4 or symbol==5:
            return 1
        
        return board[nr][nc]

    def _get_neighbors(self, r, c):

        directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1),(r+1,c+1),(r-1,c-1),(r+1,c-1),(r-1,c+1)]
        neighbors = 0
        for d in directions:
            nr,nc = d[0],d[1]
            value = self._get_neighbor_value(nr,nc) 
            neighbors += value
        
        return neighbors


    def gameOfLife(self, board) -> None:
        # step 1: iterate R C to determine the next value given neighboors
        # decoding
        # current   new   symbol
        # 0          0    2
        # 0          1    3
        # 1          0    4
        # 1          1    5

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                current = board[r][c]
                neighbors = self._get_neighbors(r,c)

                if current==0:
                    #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if neighbors==3:
                        board[r][c] = 3
                    else:
                        board[r][c] = 2
                else:

                    if neighbors in [2,3]:
                        #Any live cell with two or three live neighbors lives on to the next generation.
                        board[r][c] = 5 
                    else:
                        #Any live cell with fewer than two live neighbors dies as if caused by under-population.
                        #Any live cell with more than three live neighbors dies, as if by over-population.
                        board[r][c] = 4
        
        #step 2: decode number (2,3,4,5) to (0,1) 
        for r in range(ROWS):
            for c in range(COLS):
                new_value = board[r][c]
                if new_value in [2,4]:
                    board[r][c]=0
                elif new_value in [3,5]:
                    board[r][c]=1
                else:
                    raise ValueError("input",new_value,'is not recoginized')

if __name__=='__main__':
    print ("start...")

    s = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print ("BEFORE")
    print (board)

    s.gameOfLife(board)

    print ("AFTER")
    print (board)

    print ("END!")
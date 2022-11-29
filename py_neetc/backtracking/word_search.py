
class Solution:

    def exist(self, board, word):
        
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        word_ptr = 0
        res = [False]

        def dfs(r,c, word_ptr):

            if word_ptr==len(word):
                res[0]=True
                return True

            is_visited = (r,c) in visited
            out_of_bounds = r>=ROWS or r<0 or c>=COLS or c<0

            if is_visited or out_of_bounds:
                return False

            same_char = board[r][c]==word[word_ptr]
            if not same_char:
                return False
                
            word_ptr+=1
            visited.add((r,c))

            dfs(r+1,c,word_ptr)                                     
            dfs(r-1,c,word_ptr)                
            dfs(r,c+1,word_ptr)                
            dfs(r,c-1,word_ptr)

            visited.remove((r,c)) 
            return

        for r in range(0,ROWS):
            for c in range(0,COLS):
                if board[r][c]==word[0]:
                    dfs(r,c, word_ptr)
                    if res[0]:
                        return True       

        return False
        
        
if __name__=='__main__':
    print ("Start...")    

    s = Solution()
    word = "ABCESEEEFS"
    board = [
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]
            ]
    f = s.exist(board,word)  
    print (f)

    print ("END")

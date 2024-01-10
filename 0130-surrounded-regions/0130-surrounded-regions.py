class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(x,y):
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == "O":
                board[x][y] = "."
                for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    dfs(nx,ny)
        
        # boundary
        for i in [0,len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i,j)
        for i in range(len(board)):
            for j in [0,len(board[0])-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"
                    
        return board
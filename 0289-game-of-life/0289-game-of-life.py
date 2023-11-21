class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live, neighbors < 2 : dies
        # live, neighbors == 2 or 3 : lives
        # live, neighbors > 3 : dies
        # dead, live neighbors == 3: lives
        
        # 각 cell 마다 1개수 세고 그걸로 살고 죽이면 brute-force로 접근하는 식..
        # dead를 N-1개수로 세기엔 edge 부분이 있고....
        
        cnt = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                for x,y in (i-1,j-1),(i,j-1),(i+1,j-1),(i-1,j),(i+1,j),(i-1,j+1),(i,j+1),(i+1,j+1):
                    if x>=0 and x<len(board) and y>=0 and y<len(board[0]):
                        if board[x][y] == 1:
                            cnt[i][j] += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1: #live
                    if cnt[i][j] < 2:
                        board[i][j] = 0
                    elif cnt[i][j] == 2 or cnt[i][j] == 3:
                        board[i][j] = 1
                    elif cnt[i][j] > 3:
                        board[i][j] = 0
                else: #dead
                    if cnt[i][j] == 3:
                        board[i][j] = 1
      

                

                        
                        
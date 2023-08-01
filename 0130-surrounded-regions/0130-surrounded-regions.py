from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        # 가장자리가 board[r][c] == "O"인 칸을 queue에 넣기
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in [0,len(board)-1] or j in [0,len(board[0])-1] and board[i][j] == "O":
                    queue.append((i,j))
                    
        while queue:
            r,c = queue.popleft() #popleft는 한번에 2개를 배정할 수 있음
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O": #range 벗어나니까 조건 넣어주고
                board[r][c] = "."
                queue.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)]) #상하좌우 queue에 append. 범위가 벗어나도 그냥 넣기 어차피 위에서 range내에서만 돌기 때문에 괜찮음.
                #extend는 list로 묶어줘야함
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O": #"."으로 안 바뀐것들은 가장자리랑 상관없어서 그냥 바로 X로 바꿔도 됨. 
                    board[r][c] = "X" #"X"로 바꾸고
                elif board[r][c] == ".": #"."은 가장자리에 있는거라서 X로 못 바뀜. 
                    board[r][c] = "O" #"O"로 바꾼다..?
                    
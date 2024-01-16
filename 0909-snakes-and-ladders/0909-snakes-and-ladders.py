class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1:0}
        bfs = [1]
        for x in bfs:
            for i in range(x+1, x+7): #값으로 range를 돌고
                a,b = (i-1)//n , (i-1)%n #좌표 a,b를 계산해주기
                nxt = board[~a][b if a%2==0 else ~b] #bitwise로 
                if nxt>0: i=nxt
                if i==n*n: return need[x]+1 #도달하면 return
                #need는 이동해야할 칸수 세는것. -1인것들도 거쳐가는거면 다 +1해서 카운트
                if i not in need: 
                    need[i] = need[x]+1
                    bfs.append(i)
        return -1
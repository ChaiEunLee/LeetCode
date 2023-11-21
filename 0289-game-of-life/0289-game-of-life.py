class Solution:
    # board[I][J]에는 1이 몇개인지 세어주는 함수
    def gameOfLifeInfinite(self, live):
        # live한 index들이 들어왔으니까 그거 기준으로 개수셈
        ctr = collections.Counter((I,J)
                               for i,j in live
                                for I in range(i-1,i+2)
                                for J in range(j-1, j+2)
                                if I != i or J != j)
        
        # 그중에 다음 step에서도 live한 index들만 return
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij]==2 and ij in live}
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live, neighbors < 2 : dies
        # live, neighbors == 2 or 3 : lives
        # live, neighbors > 3 : dies
        # dead, live neighbors == 3: lives

        live = {(i,j) for i,row in enumerate(board) for j,live in enumerate(row) if live}
        # i, row <- index, row를 출력
        # j, live <- index, 각 row 값 하나씩 출력
        # if live : 출력한 값이 1인 index만 live에 들어감.
        
        # 다음 step에서 live 인것들 받음        
        live = self.gameOfLifeInfinite(live)
        
        # 다음 step에서 live인거 적용
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i,j) in live)



                

                        
                        
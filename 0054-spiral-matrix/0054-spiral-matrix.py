class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 지나가면 0으로 만들어버림.
        # len()나 0을 마주하면 방향틀기

        
        spiral = []
        i,j = 0,0
        col = True
        increase = True
        # and 를 넣을떄는 순서가 중요함
        while j<len(matrix[0]) and i<len(matrix) and matrix[i][j] != 101:
            #print(i,j,matrix[i][j],col,increase)
            spiral.append(matrix[i][j])
            matrix[i][j] = 101
            
            # i,j 길이도 보고 
            # matrix[i][j]==0이면 
            # col 이동
            if col:
                if increase: 
                    j+= 1
                else: 
                    j -= 1
                    
                if j==len(matrix[0]) or matrix[i][j]==101:
                    #row 이동 + 부호는 그대로
                    # j 원상복귀하고 
                    if increase:
                        j -= 1  
                    else:
                        j += 1
                    col = False
                    if increase: 
                        i +=1 
                    else: 
                        i-=1
            else:
                if increase: 
                    i+= 1
                else: 
                    i -= 1
                if i==len(matrix) or matrix[i][j]==101:
                    #col 이동 + 무조건 부호도 바뀌어야함.
                    # i 원상복귀하고 
                    if increase:
                        i -= 1  
                    else:
                        i += 1
                    col = True
                    increase = not increase
                    if increase:
                        j += 1  
                    else:
                        j -= 1
            #print(spiral,i,j)
        
        return spiral

                
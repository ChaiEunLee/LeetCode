class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 맨 마지막 줄에 값들 다 넣고 그 중에서 하나 꼽는거
        n = len(triangle)
        next_row = triangle[-1][:]
        curr_row = [0]*n
        for i in range(n-2,-1,-1):
            for j in range(i+1): #0~i
                #print(i,j)
                lower_left = triangle[i][j] + next_row[j] #왼
                lower_right = triangle[i][j] + next_row[j+1] #오
                curr_row[j] = min(lower_left, lower_right) # 둘중에 작은값으로
                # 맨 마지막 줄 기준으로 하니까 위로 올라가면 index가 넘어가지 않음
                # + 작은값을 위로 올리니까 맨 앞 값이 제일 작은 값
                #print(curr_row, next_row)
            curr_row, next_row = next_row, curr_row
        return next_row[0] 
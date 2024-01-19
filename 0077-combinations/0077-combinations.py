class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # bfs
        def bfs(i, comb):
            if len(comb) == k:
                answer.append(comb)
                return
            
            # i+1~n까지
            for j in range(i+1,n+1):
                bfs(j,comb+[j])
            
        answer = []
        # 0~n-k까지인데 index가 1부터라 1~n-k+1까지여야해서 range(1,n-k+2)
        for i in range(1,n-k+2): 
            bfs(i,[i])
            
        return answer
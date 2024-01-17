class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # candidates를 돌면서 dfs 시작 -> dfs(i)
        # candidates[i] 이후의 모든 조합을 찾으면 됨
        # 누적에서 쌓다가 target과 일치하면 return 커지면 stop
        # 하나의 값을 여러번 쓸 수 있음. 
        
        res = target
        answer = []
        comb = []
        
        def dfs(i, comb, res):
            if res < 0:
                return
            if res == 0:
                answer.append(comb)
                return
            elif res > 0:
                #print(i,comb, res)
                for k in range(i, len(candidates)):
                    #res -= candidates[k] # 이런식으로 반영하면 안되고
                    #print(k,comb,res)
                    dfs(k,comb+[candidates[k]], res-candidates[k]) #값만 dfs에 넣어줘야함
                    
        dfs(0, [], target)
        return answer
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            # csum(candidate sum) : 조합의 합
            # index : 순서
            # path : 지금까지의 탐색 경로
            
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path+[candidates[i]]) 
                # 입력값에 0이 있으면 i를 쓰면 무한루프가 되어서 0을 넣어서 처음부터 탐색하도록 예외 케이스를 넣어줘야하는데... 어떻게 하라는건지?
                
        dfs(target, 0, [])
        return result
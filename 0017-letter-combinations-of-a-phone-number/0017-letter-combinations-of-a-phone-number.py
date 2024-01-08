from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 자릿수가 동일할 때까지 재귀 호출 반복
        def dfs(index, path): #길이가 len(digits)인 알파벳이 완성되면 return. 
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)): #출력할 자릿수. 23이면 길이가 2인 조합만 계속 나와야하니까. 
                for j in dic[digits[i]]: #각 번호에 딸려있는 알파벳 길이가 다 다르니 그 길이만큼 다 돌면서. 
                    dfs(i+1, path+j)
                    
        if not digits:
            return []
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        dfs(0,"")
        
        return result
        
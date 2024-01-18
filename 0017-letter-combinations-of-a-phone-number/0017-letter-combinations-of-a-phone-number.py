class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 숫자-문자 연결
        phone = {'2':'abc', '3':'def','4':'ghi','5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        answer = []
        
        #dfs
        def dfs(i, comb):
            if len(comb) == len(digits):
                answer.append(comb)
                return
            for j in phone[digits[i]]:
                dfs(i+1, comb+j)
        if len(digits)>0:
            dfs(0,"")
        return answer
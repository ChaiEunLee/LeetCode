class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l)+op+str(r))) #eval: 문자열로 식을 받아서 결과를 계산해주는 함수
                    # str(l) + op + str(r)이면 left 괄호로 묶고, right 괄호로 묶은 다음 op 로 계산해주는 결과
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        for index, value in enumerate(expression): # 한칸씩 이동하면서 끊을거고,
            if value in "-+*": # 연산기호에서만 끊을것임
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                
                results.extend(compute(left, right, value)) #extend: list in list가 아니라 하나의 list로 return 하기 위해서
                
        return results
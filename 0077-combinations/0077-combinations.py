from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combi = combinations(range(1,n+1),k)
        answer = []
        for c in combi:
            answer.append(c)
        return answer
    
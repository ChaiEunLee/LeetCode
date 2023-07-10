from itertools import combinations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permu = permutations(nums,len(nums))
        answer = []
        for p in permu:
            answer.append(p)
        return answer
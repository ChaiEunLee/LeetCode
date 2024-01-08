class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            # add result when it is leaf node
            if len(elements) == 0:
                # result에 추가 
                results.append(prev_elements[:]) #copy()를 하지 않으면 reference가 됨.                 
                
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()               
                
        # Run dfs
        dfs(nums)
        return results
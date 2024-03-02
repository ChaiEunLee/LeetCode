import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(collections.Counter(tasks).values()) # counts list
        M = max(task_counts) # 제일 큰 counts 숫자
        Mct = task_counts.count(M) # 제일 큰 counts인 tasks들
        
        # Example 1
        # (nums of chunks with idles * length of a chunk with idle) + length of the final chunk # 2*3+2=8
        # nums of chunks with idles: task의 최대 interval = 3-1 = 2 = A A A면 interval은 2개니까
        # length of a chunk with idle : n+1 = 2+1 = A __ A __ A 로 되어야하니까 A의 한 chunk는 3
        # length of the final chunk : num of chars with max count = 2 = A,B 둘 다 최대길이니까 마지막에 나머지처럼 돌아갈것들
        return max(len(tasks), (M - 1) * (n + 1) + Mct) # tasks길이, (제일 긴 task 길이 -1)*(interval+1) + 제일 큰 counts tasks
        
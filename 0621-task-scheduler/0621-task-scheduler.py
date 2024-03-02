import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        
        while True:
            sub_count=0
            # 개수 순 추출
            for task, _ in counter.most_common(n+1): #최빈값 n+1개 반환. 
                sub_count+=1
                result+=1
                counter.subtract(task) #counter[task]-=1
                counter += collections.Counter() # 0이하인 아이템을 목록에서 완전히 제거. 0이하인것만 아예 빼주는 함수인듯.
            if not counter:
                break
            result += n-sub_count+1
        
        return result
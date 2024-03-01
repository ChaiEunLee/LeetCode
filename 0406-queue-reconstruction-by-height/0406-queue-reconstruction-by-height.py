class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 파이썬은 Min Heap만 지원하기 때문에 마이너스를 붙여서 Max Heap으로 구현하면 됨
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            #print(-person[0], person[1])
            heapq.heappush(heap, (-person[0], person[1]))
            #print(heapq)
            
        result = []
        while heap:
            person = heapq.heappop(heap)
            #print(person)
            result.insert(person[1], [-person[0], person[1]]) # 큰사람수, [-키, 큰사람수] # 큰사람숫자를 index로 사용?
            #print(person[1], [-person[0], person[1]])
            #print(result)
        return result
            
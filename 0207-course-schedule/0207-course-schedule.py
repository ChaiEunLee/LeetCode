class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x,y in prerequisites:
            graph[x].append(y)
            
        # cycle을 판별하기 위해 들렀던 곳을 기록하는 traced
        traced = set()
        visited = set()
        
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드면 True
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제. - 하나의 경로가 끝나면 삭제해줘야함.
            traced.remove(i)
            visited.add(i)
            
            return True
        
        # 순환구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        return True
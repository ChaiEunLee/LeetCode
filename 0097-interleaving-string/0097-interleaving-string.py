class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        stack, visited = [(0,0)], set((0,0)) #s1,s2 index
        while stack: 
            # stack을 다 쓸때까지 == x,y index가 끝까지 돌 때까지
            x,y = stack.pop()
            if x+y==l:
                return True
            if x+1<=r and s1[x] == s3[x+y] and (x+1,y) not in visited:
                stack.append((x+1,y))
                visited.add((x+1,y))
            if y+1<=c and s2[y] == s3[x+y] and (x,y+1) not in visited:
                stack.append((x,y+1))
                visited.add((x,y+1))
        return False
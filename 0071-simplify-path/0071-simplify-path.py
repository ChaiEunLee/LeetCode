class Solution:
    def simplifyPath(self, path: str) -> str:
        # .. -> previous path : ..나오면 앞의 directory를 지우기?
        # // -> / #split "/"면 자동으로 없어짐
        # 필요없는거 다 빼고 나중에 경로를 하나로 만드는 방식
        
        p = path.split("/")
        directory = []
        answer = ""

        for part in p:
            if directory and part == "..":
                directory.pop()
            elif part != "" and part != "." and part != "..":
                directory.append(part)
        
        if not directory:
            return "/"
        
        while(directory):
            cur = directory.pop()
            answer = "/" + cur + answer
            
        return answer
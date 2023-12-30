class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {')':'(', '}':'{', ']':'['} #괄호 key, value를 거꾸로
        for char in s:
            if char not in myDict: #dictioanry key에 해당하는걸 이렇게 거를수 있음
                stack.append(char)
            elif not stack or myDict[char] != stack.pop():
                return False
        return len(stack)==0 #괄호 남아있으면 false
            
import collections
class MyStack:

    def __init__(self):
        self.q = collections.deque()
        
    def push(self, x: int):
        self.q.append(x) 
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft()) #맨 뒤 빼고는 다 popleft로 빼서 맨 뒤로 append하기


    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        top = self.q[0]
        return top

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
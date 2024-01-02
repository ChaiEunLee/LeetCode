class MyQueue:  
    
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek() # peek()와 같으므로
        return self.output.pop() #pop() : default is pop(-1)

    def peek(self) -> int:
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop()) #pop(): 위에서 정의한 pop(self)이 아니라 파이썬 함수임. 
        return self.output[-1]
        
    def empty(self) -> bool:
        return self.input == [] and self.output == []        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
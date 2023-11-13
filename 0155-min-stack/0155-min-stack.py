class MinStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        popval = self.stack[-1]
        self.stack = self.stack[0:-1]
        return popval

    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
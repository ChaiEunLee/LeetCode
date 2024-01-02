class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.k = k
        self.start = 0
        self.end = 0
    def enQueue(self, value: int) -> bool:
        #print(self.q, self.end, self.k)
        if self.q[self.end] is None:
            self.q[self.end] = value
            self.end = (self.end+1) % self.k # 이렇게 한번에..
            return True
        return False

    def deQueue(self) -> bool:
        #print(self.q, self.end, self.k)
        if self.q[self.start] is None:
            return False
        else:
            self.q[self.start] = None
            self.start = (self.start+1) % self.k
            return True

    def Front(self) -> int:
        return -1 if self.q[self.start] is None else self.q[self.start]

    def Rear(self) -> int:
        return -1 if self.q[self.end-1] is None else self.q[self.end-1]
        
    def isEmpty(self) -> bool:
        return self.start == self.end and self.q[self.start] is None
            
    def isFull(self) -> bool:
        return self.start == self.end and self.q[self.start] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
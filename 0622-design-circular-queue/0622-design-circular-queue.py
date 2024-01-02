class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for _ in range(k)]
        self.k = k
        self.start = 0
        self.end = 0
    def enQueue(self, value: int) -> bool:
        #print(self.q, self.end, self.k)
        if self.q[self.end] == -1:
            self.q[self.end] = value
            self.end += 1
            if self.end == self.k:
                self.end = 0
            return True
        return False

    def deQueue(self) -> bool:
        #print(self.q, self.end, self.k)
        if self.q[self.start] > -1:
            self.q[self.start] = -1
            self.start += 1            
            if self.start == self.k:
                self.start = 0
            return True
        return False

    def Front(self) -> int:
        return self.q[self.start]

    def Rear(self) -> int:
        if self.end > 0:
            rearindex = self.end-1
        else:
            rearindex = self.k-1
        return self.q[rearindex]

    def isEmpty(self) -> bool:
        if self.start == self.end and self.q[self.start] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.end == self.start and self.q[self.end] > -1:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
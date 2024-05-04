class MyQueue:
    def __init__(self):
        self.front = None
        self.back = None
        self.queue = []

    def push(self, x: int) -> None:
        if not self.back:
            self.front = self.back = x
        else:
            self.back = x
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) == 2:
            self.front = self.back = self.queue[-1]
        elif len(self.queue) < 2:
            self.front = self.back = None
        else:
            self.front = self.queue[1]
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.front
        
    def empty(self) -> bool:
        return False if self.queue else True
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

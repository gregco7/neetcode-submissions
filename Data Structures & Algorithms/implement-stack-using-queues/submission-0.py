class MyStack:

    def __init__(self):
        self.q1 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        iterations = len(self.q1) - 1
        for i in range(iterations):
            self.push(self.q1.popleft())
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#Stack follows LIFO Principles: Last in, First Out
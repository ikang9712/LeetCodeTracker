from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.windowSize = size
        self.values = deque([])

    def next(self, val: int) -> float:
        self.values.append(val)
        if len(self.values) > self.windowSize:
            self.values.popleft()
        return sum(self.values) / len(self.values)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
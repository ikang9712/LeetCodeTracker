class MovingAverage:

    def __init__(self, size: int):
        self.windowSize = size
        self.values = []

    def next(self, val: int) -> float:
        if len(self.values) < self.windowSize:
            self.values.append(val)
            return sum(self.values) / len(self.values)
        else:
            self.values = self.values[1:] + [val]
            return sum(self.values) / self.windowSize



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
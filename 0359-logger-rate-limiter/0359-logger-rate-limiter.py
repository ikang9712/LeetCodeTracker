class Logger:

    def __init__(self):
        self.dict = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.dict[message]:
                self.dict[message] = timestamp + 10
                return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
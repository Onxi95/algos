class Logger:

    def __init__(self):
        self.memory = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.memory:
            self.memory[message] = timestamp
            return True
        else:
            prev_timestamp = self.memory.pop(message)
            if timestamp - prev_timestamp >= 10:
                self.memory[message] = timestamp
                return True
            self.memory[message] = prev_timestamp
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

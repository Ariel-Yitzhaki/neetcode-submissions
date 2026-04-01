class MinStack:

    def __init__(self):
        self.s = []
        self.mini = 0
        
    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.mini = val
        else:
            self.s.append(val - self.mini)
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        pop = self.s.pop()
        if pop < 0:
            self.mini = self.mini - pop

    def top(self) -> int:
        if self.s[-1] < 0:
            return self.mini
        else:
            return self.s[-1] + self.mini

    def getMin(self) -> int:
        return self.mini

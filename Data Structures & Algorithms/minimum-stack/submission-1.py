class MinStack:

    def __init__(self):
        self.s, self.t = [], []
        self.t.append(2**31 - 1)
    def push(self, val: int) -> None:
        if self.t[-1] >= val:
            self.t.append(val)
        self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.t[-1]:
            self.t.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.t[-1]

class MinStack:
    def __init__(self):
        self.stack = []
        self.m_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.m_stack or self.m_stack[-1] >= val:
            self.m_stack.append(val)

    def pop(self) -> None:
        if self.m_stack[-1] == self.stack[-1]:
            self.m_stack = self.m_stack[:-1]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m_stack[-1]
        

class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []
    def push(self,val):
        min_val = min(val, self.mstack[-1]) if self.mstack else val
        self.mstack.append(min_val)
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
        self.mstack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mstack[-1]
        

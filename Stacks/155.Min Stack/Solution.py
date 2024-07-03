class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) < 1 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)
        
        

    def pop(self):
        if len(self.min_stack) > 0 and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
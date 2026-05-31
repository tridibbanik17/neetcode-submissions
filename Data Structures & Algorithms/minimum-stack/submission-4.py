class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1

    def pop(self) -> None:
        last_element = self.stack[self.length - 1]
        del self.stack[-1]
        self.length -= 1

    def top(self) -> int:
        last_element = self.stack[self.length - 1]
        return last_element

    def getMin(self) -> int:
        # return min(self.stack)
        min_element = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < min_element:
                min_element = self.stack[i]
        return min_element
        

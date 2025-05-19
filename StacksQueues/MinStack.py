## O(1) time O(n) space
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        c = self.stack[-1]
        return c

    def getMin(self) -> int:
        return self.min_stack[-1]
    
## define stack and min_stack in constructor
## push function appends val to stack, but only append val to min_stack if min_stack is empty, or val <= to the top val of min_stack
##pop function pops the top of the stack, but only pop min_stack if the val you popped from the stack is equal to the top val of min_stack
##top function returns the top val of stack
##min_stack should have a stack from increasing to decreasing so return the top of min_stack to for getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
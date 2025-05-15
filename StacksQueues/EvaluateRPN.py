## O(n) time O(n) space

class Solution(object):
    def evalRPN(self, tokens):
        operators = ["+", "-", "*", "/"]
        stk = []
        for token in tokens:
            if token not in operators:
                stk.append(int(token))
            elif token == "+":
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b+a)
            elif token == "-":
                c = int(stk.pop())
                d = int(stk.pop())
                stk.append(d-c)
            elif token == "*":
                e = int(stk.pop())
                f = int(stk.pop())
                stk.append(f*e)
            elif token == "/":
                g = int(stk.pop())
                h = int(stk.pop())
                stk.append(int(float(h)/g))
    
        return stk[0]


## postfix to infix problem
## initialize an empty stack as well as an array with the operators
## iterate through the tokens
## if the token is a number push the number to the stack
## if the token is an operation, pop the last two numbers in the stack and perform the operation on them. then append the result to the stack
## and the end there should only be one number in the stack which is the result , return that number
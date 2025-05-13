class Solution(object):
    def isValid(self, s):
        pairs = {"(": ")", "{": "}", "[": "]"}
        valid = []
        for char in s:
            if char in pairs:
                valid.append(char)
            else:
                if not valid:
                    return False
                c = valid.pop()
                if char != pairs[c]:
                    return False
        return not valid
    
## hash map with all the pairs
## initlialize a stack named valid 
## loop through each char in s:
## if the char is an opening character ( (, [, {) then push the character to the stack
## if the char is a closing character ( ), ], }) then check if the last char in the stack is equal to the current closing character in the hashmap
    ## do this by poping from the stack
## if there not equal return false
## if the stack is empty (that means there is no opening chars) then return False
## if successfull the stack should be empty, so return not stk
class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append((t, i))
        return answer
    

    ## answer is result array
        ## stack is storing tuples of temperature(t), index(i)
        ## while the stack is not empty and the top of the stack's first value in the tuple (the temperature) is LESS than the current temperature
            ## pop off the tuple
            ## sett answer at the old index equal to current index - the old index
        ## always add the append the tuple of the current index and temp
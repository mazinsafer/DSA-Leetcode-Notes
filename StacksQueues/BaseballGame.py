def calPoints(self, operations):
        record = [] ## list to keep track of opeations
        for operation in operations: ## iterate through operations
            if operation == "+":
                record.append(int(record[-1] + (record[-2]))) ## add sum of last two scores
            if operation == "C":
                record.pop() ## remove last score
            if operation == "D":
                record.append(int(2*(record[-1])))   ## add double last score
            elif operation not in ("+", "C", "D"):
                record.append(int(operation))
        return sum(record) # return the sum of all the scores


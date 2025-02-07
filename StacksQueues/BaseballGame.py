def calPoints(self, operations):
        record = []
        output = 0
        for operation in operations:
            if operation == "+":
                record.append(int(record[-1] + (record[-2])))
            if operation == "C":
                record.pop()
            if operation == "D":
                record.append(int(2*(record[-1])))
            elif operation not in ("+", "C", "D"):
                record.append(int(operation))
        return sum(record)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        
        for op in operations:
            if op == "D":
                # Double the last score in our record
                lst.append(lst[-1] * 2)
            elif op == "+":
                # Sum the last two scores in our record
                lst.append(lst[-1] + lst[-2])
            elif op == "C":
                # Remove the last score
                lst.pop()
            else:
                # It's a number (positive or negative), convert and append
                lst.append(int(op))
           
        # Sum up all integers in our record
        return sum(lst)
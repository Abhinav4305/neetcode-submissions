class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        
        for op in operations:
            if op == "D":
                lst.append(lst[-1] * 2)
            elif op == "+":
                lst.append(lst[-1] + lst[-2])
            elif op == "C":
                lst.pop()
            else:
                lst.append(int(op))
           
        return sum(lst)
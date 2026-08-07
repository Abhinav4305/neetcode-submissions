class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        sum = 0
        for i in range(len(operations)):
            if operations[i] in ['0','1','2','3','4','5','6','7','8','9']:
                lst.append(int(operations[i]))
            elif operations[i] == "D":
                lst.append(int(lst[-1])*2)
            elif operations[i] == "+":
                lst.append(int(lst[i-1])+int(lst[i-2]))
            elif operations[i] == "C":
                lst.pop()
           
        
        for i in range(len(lst)):
            sum += int(lst[i])
        return sum
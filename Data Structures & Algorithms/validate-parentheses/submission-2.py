class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char in "({[":
                stk.append(char)
            elif char == ")" :
                if not stk or stk[-1] != "(":
                    return False
                stk.pop()
            elif char == "]" :
                if not stk or stk[-1] != "[":
                    return False
                stk.pop()
            elif char == "}" :
                if not stk or stk[-1] != "{":
                    return False
                stk.pop()
            else:
                return False

        return len(stk) == 0
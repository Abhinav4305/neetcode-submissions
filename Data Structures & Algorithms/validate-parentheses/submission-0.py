class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == "{" or "[" or "(":
                stk.append(char)
            if char == "}":
                if "{" in stk:
                    return True
                else:
                    False
            if char == "]":
                if "[" in stk:
                    return True
                else:
                    return False
            if char == ")":
                if "(" in stk:
                    return True
                else:
                    return False

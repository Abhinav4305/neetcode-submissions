class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = {']':'[', ')':'(', '}':'{'}
        for char in s:
            if char in brackets:
                if stk and stk[-1] == brackets[char]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)

        return True if not stk else False
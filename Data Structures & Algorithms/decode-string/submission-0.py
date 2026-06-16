class Solution:
    def decodeString(self, s: str) -> str:
        count_stk = []
        string_stk = []
        cur = ""
        k = 0


        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
                
            elif c == "[":
                string_stk.append(cur)
                count_stk.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = string_stk.pop()
                count = count_stk.pop()
                cur += temp*count
            else:
                cur += c
        return cur
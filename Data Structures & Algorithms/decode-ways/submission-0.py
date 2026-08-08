class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) > 1 and s[0] != "0":
            return len(s)
        else:
            return 0

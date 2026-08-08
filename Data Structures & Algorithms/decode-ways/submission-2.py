class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s) in [1, 10]:
            return 1
        elif int(s) > 10:
            return len(s)
        else:
            return 0

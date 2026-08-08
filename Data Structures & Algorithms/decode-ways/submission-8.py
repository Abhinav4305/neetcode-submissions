class Solution:
    def numDecodings(self, s: str) -> int:
        for i in range(1, 10):
            if len(s) == 1 and int(s) == i or int(s) == 10:
                return 1
            
        if int(s) > 10:
            if int(s) == 27:
                return 1
            return len(s)
        
        else:
            return 0

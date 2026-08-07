class Solution:
    def mySqrt(self, x: int) -> int:
        while x>0:
            for i in range(x):
                if i**2 > x :
                    return i-1
                elif i**2 < x: 
                    continue
        return 0
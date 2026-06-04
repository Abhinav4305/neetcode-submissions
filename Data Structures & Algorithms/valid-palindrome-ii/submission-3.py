class Solution:
    def validPalindrome(self, s: str) -> bool:
        lst = list(s)
        n = len(lst)
        if lst == lst[::-1]:
            return True
        else :
            for i in range(n//2):
                if lst[i] != lst[n-1-i]:
                    option_a = lst[:i] + lst[i+1:]
                    option_b = lst[:n-i-1] + lst[n-i:]
                    return (option_a == option_a[::-1]) or (option_b == option_b[::-1])
            return True
        
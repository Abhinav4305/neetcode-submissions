class Solution:
    def validPalindrome(self, s: str) -> bool:
        lst = list(s)
        n = len(lst)
        if lst == lst[::-1]:
            return True
        else :
            for i in range((n-1)//2):
                if lst[i] != lst[n-1-i]:
                    lst.pop(n-i-1)
                    i+=1
                    if lst != lst[::-1]:
                        return False
            return True
        
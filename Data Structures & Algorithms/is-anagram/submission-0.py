class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = list(s)
        lst2 = list(t)
        if sorted(lst1) == sorted(lst2):
            return True
        else:
            return False

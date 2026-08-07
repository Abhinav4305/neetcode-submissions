class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = list(s)
        s2 = []
        count = 0
        for i in range(1, len(s)):
            if s1[i] != s1[i-1]:
                s2.append(s[i])
            else:
                continue
        if len(set(s2)) == 0:
            return 1
        else:
            return len(set(s2))
        
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = []
        l = 0
        maxLen = 0
        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[l])
                l += 1
            s1.append(s[i])
                
            
            maxLen = max(maxLen, i-l+1)
        return maxLen

        
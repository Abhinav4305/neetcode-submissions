class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count = 0
        for char in text1:
            if char in text2:
                count += 1
        return count
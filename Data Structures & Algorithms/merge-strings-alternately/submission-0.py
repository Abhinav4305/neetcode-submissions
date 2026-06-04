class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        n = len(word1)
        m = len(word2)
        if n==m:
            for i in range(n):
                lst.append(word1[i])
                lst.append(word2[i])
            
        elif m>n:
            for i in range(n):
                lst.append(word1[i])
                lst.append(word2[i])
            lst.append(word2[n:m])
            
        else:
            for i in range(m):
                lst.append(word1[i])
                lst.append(word2[i])
            lst.append(word1[m:n])
        return "".join(lst)


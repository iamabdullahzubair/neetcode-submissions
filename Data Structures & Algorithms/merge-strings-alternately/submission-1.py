class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        ans = ""
        minm = min(len(word1), len(word2))

        for k in range(minm * 2):
            if k % 2 == 0:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1
        return ans

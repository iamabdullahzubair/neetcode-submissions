class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            return True
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return check(i+1, j) or check(i, j-1)

            i += 1
            j -= 1

        return True
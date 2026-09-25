class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ls = s.lower()
        clean_text = re.sub(r'\W+', '', ls)

        i = 0
        j = len(clean_text) - 1

        while i<j:
            if clean_text[i] != clean_text[j]:
                return False
            i+=1
            j-=1
        return True
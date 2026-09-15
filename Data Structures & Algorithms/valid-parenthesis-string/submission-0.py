class Solution:
    def checkValidString(self, s: str) -> bool:

        left = []
        stars = []

        for i in range(len(s)):

            if s[i] == '(':
                left.append(i)

            elif s[i] == '*':
                stars.append(i)

            else:  # ')'

                if left:
                    left.pop()

                elif stars:
                    stars.pop()

                else:
                    return False

        # Match remaining '(' with '*' appearing after them
        while left:
            if not stars:
                return False

            if left.pop() > stars.pop():
                return False

        return True
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            l = min(heights[right], heights[left])
            b = right - left
            ans = max(ans, l * b)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return ans

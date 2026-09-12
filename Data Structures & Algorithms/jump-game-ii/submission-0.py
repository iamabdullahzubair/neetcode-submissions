class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums) - 1

        l = r = 0
        res = 0

        while r < n:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(nums[i] + i, farthest)
            l = r + 1
            r = farthest
            res += 1
        return res

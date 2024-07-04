class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        if N <= 4: return 0
        distance = N - 4
        res = float('inf')
        for i in range(N - distance):
            res = min(res, nums[i + distance] - nums[i])
        return res

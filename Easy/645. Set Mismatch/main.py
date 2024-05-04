class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = 0, 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                dup = nums[i]
            if nums[i+1] - nums[i] > 1:
                miss = nums[i] + 1
        if 1 not in nums:
            miss = 1
        elif miss == 0:
            miss = len(nums)
        return [dup, miss]

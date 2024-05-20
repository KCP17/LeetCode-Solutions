class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = sum(nums)
        for amount in range(2, len(nums) + 1):
            subsets = combinations(nums, amount)
            for sub in subsets:
                total = sub[0]
                for i in range(1, len(sub)):
                    total ^= sub[i]
                res += total
        return res

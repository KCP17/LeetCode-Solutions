class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        avg = len(nums) // 2
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > avg:
                return n

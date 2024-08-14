class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sorted_dists = [0 for _ in range(max(nums) + 1)]
        for i in range(N):
            for j in range(i + 1, N):
                sorted_dists[abs(nums[i] - nums[j])] += 1
        for i, freq in enumerate(sorted_dists):
            if freq >= k:
                return i
            else:
                k -= freq

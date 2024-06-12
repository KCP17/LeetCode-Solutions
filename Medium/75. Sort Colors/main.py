class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort (bucket sort)
        num_cnt = [0, 0, 0] # Color --maps to--> frequency. Index 0 is red, 1 is white, 2 is blue
        for n in nums:
            num_cnt[n] += 1
        # Modify the input array based on the count of colors
        cur = 0
        for color in range(3): # 3 colors: 0 1 2
            times = num_cnt[color]
            for _ in range(times):
                nums[cur] = color
                cur += 1 # move to next index of the input array

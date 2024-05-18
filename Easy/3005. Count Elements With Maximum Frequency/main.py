class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total, max_freq = 0, 0 # Total frequency to return & max_freq to keep track of the current max
        freq_map = defaultdict(int) # Counter dict
        for n in nums:
            freq_map[n] += 1 # Increase the frequency of each number as we see them
            if freq_map[n] > max_freq: # If the frequency of current number is greater than the previous max frequency we've seen before
                total = max_freq = freq_map[n] # That means the current frequency becomes the max frequency, and `total` is also the current max frequency
            elif freq_map[n] == max_freq: # We've added 1 to frequency of current number above but if it's still equal to the previous max frequency 
                total += max_freq # That means there're 2 max frequencies (the previous & current one) so we add them together
        return total

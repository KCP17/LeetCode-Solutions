class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of every number
        count = Counter(nums)
        # Maps each frequency to a list of numbers of that frequency
        freq_map = defaultdict(list)
        for n, occ in count.items():
            freq_map[occ].append(n)
        # Sort the frequency values in ascending order
        sorted_map = sorted(list(freq_map.items()))
        # Adding the numbers to our result list
        res = []
        for freq, numbers in sorted_map:
            for each in sorted(numbers, reverse=True): # Sort the same-frequency numbers in descending order, and iterate through each of those sorted numbers
                for _ in range(freq):
                    res.append(each) # Append a number "its frequency" times
        return res

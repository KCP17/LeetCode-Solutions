class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: # Counting sort (Bucket sort)
        num_cnt = [0] * 1001 # Numbers of `arr1` --maps to--> their frequencies (1001 because of the constraints)
        for n in arr1:
            num_cnt[n] += 1
        
        def appending(arr):
            for n in arr:
                if len(self.res) == len(arr1): break # Enough
                times = num_cnt[n] # Frequency of that number
                for _ in range(times):
                    self.res.append(n) # Append all occurrences of that number
                num_cnt[n] = 0 # Already appended all occurrences of that number, modify to 0 to deny appending redundant numbers later

        self.res = []
        appending(arr2) # Append all numbers in `arr2` to `res` in relative order
        appending(range(1001)) # Append the rest of `arr1` in ascending order
        return self.res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cnt_1 = Counter(nums1) # Maps each number to its frequency
        cnt_2 = Counter(nums2) # Same with the one above
        for n in cnt_1.keys(): # Get all numbers in `nums1`
            if n in cnt_2: # If that also exists in `nums2` (Exists in both arrays)
                freq = min(cnt_1[n], cnt_2[n]) # We only go for the smaller frequency between 2 arrays because using the higher results in insufficient frequency of the other array
                for _ in range(freq):
                    res.append(n) # Append "lower frequency" times of `n`
        return res # Return result

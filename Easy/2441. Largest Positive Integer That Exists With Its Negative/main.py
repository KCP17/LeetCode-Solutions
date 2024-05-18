class Solution:
    def findMaxK(self, nums: List[int]) -> int: # Two pointers
        nums.sort() # Negative integer with max abs value (|-|) on the left, whereas the max positive integer (+) on the right
        l, r = 0, len(nums) - 1 # left & right pointers -> We go from both ends to inside to get the max value
        
        while nums[l] < 0 and nums[r] > 0: # Ensure the left pointer always points to a negative integer (-) & right pointer always points to a positive integer (+)
            neg, pos = abs(nums[l]), nums[r] # Get the absolute value of negative number (-), and positive number (+) -> for easier comparison
            if neg == pos: # If abs of negative (|-|) matches positive (+) -> Found
                return pos # Return the positive (+) number
            elif neg < pos: # The positive number (+) is too large compared to the corresponding abs of negative number (|-|) which left pointer is pointing at
                r -= 1 # Get a smaller positive number (+) by moving right pointer inside
            else: # The abs of negative number (|-|) is too large compared to the corresponding positive number (+) which right pointer is pointing at
                l += 1 # Get a smaller abs of negative number (|-|) by moving left pointer inside
        
        return -1 # Not found

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int: # Refer to Neetcode's explanation of 523. Continuous Subarray Sum
        '''
        A valid subarr contains contiguous elements between the two SAME accumulated remainders (a remainder is seen twice) - Not include the 1st remainder but include the 2nd
        '''
        res = 0
        pre_sum = 0 # Prefix sum
        seen_count = defaultdict(int) # remainder -maps to-> number of seen times (count)
        seen_count[0] = 1
        
        for n in nums:
            pre_sum += n # Accumulate prefix sum
            remainder = pre_sum % k # Accumulated remainder at each prefix sum
            
            res += seen_count[remainder] # The number of subarrs increased at each index is also the number of times this same remainder is seen 
            seen_count[remainder] += 1 # Increment the count of this remainder
        
        return res

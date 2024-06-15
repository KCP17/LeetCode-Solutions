class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 1. Counting (bucket) sort
        max_index = max(nums) + 1
        nums_cnt = [0] * max_index
        for n in nums:
            nums_cnt[n] += 1
        
        # 2. Count the moves
        res = 0
        carry = 0
        for occ in nums_cnt:
            res += carry
            if occ == 0:
                if carry > 0:
                    carry -= 1
            else:
                carry += (occ - 1)
        
        # 3. Add remaining moves
        if carry > 0:
            res += ((1 + carry) * (carry / 2))
        
        # 4. Return result
        return int(res)

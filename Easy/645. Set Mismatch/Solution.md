## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/105a4c73-6a00-4eab-a068-1d67a0258ee4)

## Code (Python3)
```python3 []
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = 0, 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                dup = nums[i]
            if nums[i+1] - nums[i] > 1:
                miss = nums[i] + 1
        if 1 not in nums:
            miss = 1
        elif miss == 0:
            miss = len(nums)
        return [dup, miss]
```
## Note:
Logic (My solution):
- Time: $$O(N * log(N))$$
- Space: $$O(1)$$

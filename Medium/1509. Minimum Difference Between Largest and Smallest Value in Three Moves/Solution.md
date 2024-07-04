## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/87ff347d-a7b2-4812-945a-bc2a5ae659e6)

## Code
### Python3
```python []
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        if N <= 4: return 0
        distance = N - 4
        res = float('inf')
        for i in range(N - distance):
            res = min(res, nums[i + distance] - nums[i])
        return res
```

## Note:
Sorting & Greedy (My solution):
- Time: $$O(n*log(n) + n)$$
- Space: $$O(n)$$

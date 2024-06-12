## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/1d95c0b2-f014-4aaa-bc6e-66cdd586728a)

## Code (Python3)
```python3 []
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
```
## Note:
Counting sort - doesn't satisfy follow-up question (My solution):
- Time: $$O(2n)$$
- Space: $$O(n)$$
[ Time taken: 6 m 18 s ]

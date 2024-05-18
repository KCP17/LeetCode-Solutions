## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/c7f90730-c532-416e-bd34-a71c0b256a5e)

## Code (Python)
```python []
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0] * nums[1])
```
## Note:
Sorting (my solution):
- Time: $$O(n * log (n))$$
- Space: $$O(1)$$

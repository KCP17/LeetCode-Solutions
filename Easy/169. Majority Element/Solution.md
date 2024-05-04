## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e6d37092-2e32-4cec-af39-5173a5ac5aff)

## Code (Python3)
```python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        avg = len(nums) // 2
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > avg:
                return n
```
## Time & Space:
* Time: $$O(N)$$
* Space: $$O(N)$$ doesn't satisfy follow-up requirements

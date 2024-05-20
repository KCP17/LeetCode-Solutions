## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/dbe0ae3d-0b36-4102-ab0a-03a84e0b021f)

## Code (Python3)
```python3 []
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = sum(nums)
        for amount in range(2, len(nums) + 1):
            subsets = combinations(nums, amount)
            for sub in subsets:
                total = sub[0]
                for i in range(1, len(sub)):
                    total ^= sub[i]
                res += total
        return res
```
## Note:
Brute force (My solution):
- Time: $$\sum_{k=1}^{n} k * C^k_n$$
- Space: $$\sum_{k=1}^{n} C^k_n$$

## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/1b152ab5-789d-409b-91fd-ecd0294c88ba)

## Code (Python3)
```python3 []
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```
## Note:
Intersection method (My solution):
- Time: $$O( N + M + min(N,M) )$$ with N, M length of two lists
- Space: $$O( N + M + min(N,M) )$$

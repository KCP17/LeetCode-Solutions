## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/1f3d315b-deab-4b8a-88de-a5f4d8632888)

## Code (Python3)
```python3 []
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = set()
        for occ_val in Counter(arr).values():
            if occ_val not in mem: mem.add(occ_val)
            else: return False
        return True
```
## Note:
Hashmap - checking sequentially (My solution):
- Time: $$O(N)$$
- Space: $$O(N)$$

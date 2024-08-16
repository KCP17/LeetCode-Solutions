## 1. Efficiency (Python3)
![image](https://github.com/user-attachments/assets/4066f8e8-e3f8-463f-8a4c-6f6b52c8c1f3)

## 2. Code (Python3)
```python3 []
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mx = sec_mx = (float('-inf'), -1) # Value & index of array it belongs to
        mn = sec_mn = (float('inf'), -1)

        for i, arr in enumerate(arrays):
            if arr[-1] > mx[0]:
                sec_mx = mx
                mx = (arr[-1], i)
            elif arr[-1] > sec_mx[0]:
                sec_mx = (arr[-1], i)
            
            if arr[0] < mn[0]:
                sec_mn = mn
                mn = (arr[0], i)
            elif arr[0] < sec_mn[0]:
                sec_mn = (arr[0], I)

        if mx[1] != mn[1]:
            return abs(mx[0] - mn[0])
        else:
            return max(abs(sec_mx[0] - mn[0]), abs(mx[0] - sec_mn[0]))
```

## 3. Note:
[ Time taken: 15 m 3 s ]
Greedy (My solution):
- Time: $$O(n)$$
- Space: $$O(1)$$

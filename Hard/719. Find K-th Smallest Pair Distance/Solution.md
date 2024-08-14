## 1. Efficiency - Python3
![image](https://github.com/user-attachments/assets/9cba87d4-682a-40d6-9fc6-653d7f80cbc7)

## 2. Code - Python3
```python3 []
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sorted_dists = [0 for _ in range(max(nums) + 1)]
        for i in range(N):
            for j in range(i + 1, N):
                sorted_dists[abs(nums[i] - nums[j])] += 1
        for i, freq in enumerate(sorted_dists):
            if freq >= k:
                return i
            else:
                k -= freq
```

## 3. Note:
Brute force + Bucket sort (My solution):
- Time: $$O(N^2 + max(nums) + 1)$$
- Space: $$O(max(nums) + 1)$$

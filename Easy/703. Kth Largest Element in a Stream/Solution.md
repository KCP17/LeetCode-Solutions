## 1. Efficiency (Python3)
![image](https://github.com/user-attachments/assets/17746027-27f2-49d6-bce0-f63dad73a876)

## 2. Code (Python3)
```python3 []
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val: int) -> int:
        i = bisect_left(self.nums, val)
        self.nums.insert(i, val)
        return self.nums[len(self.nums) - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

## 3. Note:
Binary search (My solution):
- Time: $$O((n+log(n))*m)$$ with `n` length of original stream, and `m` added elements
- Space: $$O(n)$$

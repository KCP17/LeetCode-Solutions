# Beats 99.93%✅🔥🔥| Python 💻 | CLEAR Explanation📗

## 1. Proof (Python3)
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/7fc6fc48-4116-4926-b319-31abb93f2990_1718074705.3675582.png)

## 2. Algorithms
* Counting Sort

## 3. Code - Python3 (with inline explanation)
```python3 []
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: # Counting sort (Bucket sort)
        num_cnt = [0] * 1001 # Numbers of `arr1` --maps to--> their frequencies (1001 because of the constraints)
        for n in arr1:
            num_cnt[n] += 1
        
        def appending(arr):
            for n in arr:
                if len(self.res) == len(arr1): break # Enough
                times = num_cnt[n] # Frequency of that number
                for _ in range(times):
                    self.res.append(n) # Append all occurrences of that number
                num_cnt[n] = 0 # Already appended all occurrences of that number, modify to 0 to deny appending redundant numbers later

        self.res = []
        appending(arr2) # Append all numbers in `arr2` to `res` in relative order
        appending(range(1001)) # Append the rest of `arr1` in ascending order
        return self.res
```

## 4. Complexity
- Time complexity: $$O(M + N)$$ - Length of 2 arrays
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$ - A mapping array of size 1001
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/relative-sort-array/solutions/5292700/beats-99-93-python-clear-explanation) if you find this solution helpful, thank you 🤍

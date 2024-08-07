# Beats 98.27%✅🔥| Python, C++💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/3b07638b-70a7-4ec3-be66-d1e2315231f9_1723043076.9180608.png)

## 2. Algorithms
* HashMap
* Counting

## 3. Code (with inline explanation)
```python3 []
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = Counter(arr)
        for s in arr:
            if freq_map[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
```

## 4. Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(n)$$

### Upvote if you find this solution helpful, thank you 🤍

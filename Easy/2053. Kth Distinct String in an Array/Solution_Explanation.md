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
        freq_map = Counter(arr) # a Counting HashMap that maps each letter to its frequency
        for s in arr:
            if freq_map[s] == 1: # If a letter appears only once (aka it has the frequency of 1)
                k -= 1 # Decrement `k` until..
                if k == 0: # `k` reaches 0, means this is the Kth appear-once letter
                    return s # Return that letter
        return "" # If no letter had been returned, then return an empty string
```

## 4. Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(n)$$

### Upvote [here](https://leetcode.com/problems/kth-distinct-string-in-an-array/solutions/5602876/beats-98-27-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

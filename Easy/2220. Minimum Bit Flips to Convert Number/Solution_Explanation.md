# Beats 97.89%✅🔥| Python, C++💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/35a04ca5-4ec6-439c-80b2-8060abffdb8a_1726106480.9847486.png)

## 2. Algorithms
* XOR

## 3. Code (with inline explanation)
```python3 []
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR `start` and `goal` to get all `1`s in the columns where start[i] != goal[i]
        xor = bin(start ^ goal)
        # Count the `1`s (aka the differences that need to be flipped)
        return xor.count('1')
```

## 4. Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/solutions/5773772/beats-97-89-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

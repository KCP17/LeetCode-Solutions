# Beats 95.67%✅🔥| Python💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/21161b18-8367-41bb-a6a1-9f264a4b50b6_1724379442.6680021.png)

## 2. Algorithms
* Binary conversion

## 3. Code - Python3 (with inline explanation)
```python3 []
class Solution:
    def findComplement(self, num: int) -> int:
        # Suppose the number of bits in binary representation of `num` is `n`
        # So `n = len(bin(num)) - 2` (subtract by 2 to omit "0b")
        # We perform 2**n to get the value of the bit at index `n`
        # Then subtract by 1 to get the total values where all `n` bits are `1`
        # Finally, we subtract that by `num` to get its complement
        return (2**(len(bin(num)) - 2) - 1) - num
```

## 4. Complexity
- Time complexity: $$O(1)$$
- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/number-complement/solutions/5677244/beats-95-67-python-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

# Beats 95.58%✅🔥| Python💻| SUPER EASY Solution📕

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/3ee7e34a-dd96-43b1-9dd6-72eb0cb13913_1722526388.2966347.png)

## 2. Algorithms
* Simple array traversal

## 3. Code - Python3 (with inline explanation)
```python3 []
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 1-10 (phone) --> 11 (gender) --> 12-13 (age) --> 14-15 (seat)
        res = 0
        for passenger in details:
            if int(passenger[11 : 13]) > 60: # If digits 12 & 13 (indices 11 & 12), which indicates the age
                res += 1
        return res
```

## 4. Complexity
- Time complexity: $$O(N)$$
- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/number-of-senior-citizens/solutions/5569835/beats-95-58-python-super-easy-solution) if you find this solution helpful, thank you 🤍

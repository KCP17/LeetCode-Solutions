# 0ms - BEATS 100% - CONSTANT TIME & SPACE 🔥🔥🔥| Python, C++ (Math🔢) | SUPER EASY Explanation ✅

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image.png](https://assets.leetcode.com/users/images/0d978a48-273d-446f-9396-1266a868ffde_1710304323.0200264.png)
### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/0249993d-a6f9-4391-8f1b-6a866c65ba75_1710304371.24554.png)

## 2. Approach - Explanation
<!-- Describe your approach to solving the problem. -->
1. For an **Arithmetic Progression: $$a+...+b$$**, we can calculate the sum of that sequence using the formula: $$\frac{(a+b)\cdot n}{2}$$ with *a* is the first number, *b* is the last number in the sequence, and *n* is the number of numbers of that sequence.
2. Now we want to find `x` (the pivot) and the condition is `sum_left` (sum from 1 to x) must be equal with `sum_right` (sum from x to n). So, we're going to build a formula to find `x` based on that given condition. Here is how to build that formula:

![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e69fb770-a7ac-4be4-a849-e89ded87fa87)

We found that `x` is the square root of sum of the sequence from 1 to n (that's interesting !!!) but this fact is not really that important is it? Because eventually, we found our formula to calculate the pivot and that's the crucial part.
3. Finally, just return the pivot. However, what if the `x` that we calculated is not an integer? What if it's something like 5.6? That's definitely not a valid pivot right? Yeah, and that tells us the sequence does not have a pivot, so just return `-1`. In other cases where `x` is an integer then we can safely return `x` as it's a valid pivot.

## 3. Complexity
- Time complexity: $$O(1)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 4. Code

### 4.1. Python3
```python3 []
class Solution:
    def pivotInteger(self, n: int) -> int: # Arithmetic Progression
        x = sqrt((n * (n + 1)) / 2)
        return int(x) if int(x) == x else -1
```

### 4.2. C++
``` cpp []
class Solution {
public:
    int pivotInteger(int n) {
        float x = sqrt((n * (n + 1)) / 2);
        return ((int)x == x ? (int)x : -1);
    }
};
```

### Upvote [here](https://leetcode.com/problems/find-the-pivot-integer/solutions/4867702/0ms-beats-100-constant-time-space-python-c-math-super-easy-explanation) if you find this solution helpful, thank you 🤍

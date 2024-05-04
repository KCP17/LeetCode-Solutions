# 0ms - Beats 100% 🔥🔥🔥| EASIEST approach - NO Loops/Recursion, just SIMPLE MATH 🔢 | Python, C++ 💻

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/14ddae6b-abd5-4365-8f95-7b7577d53f52_1714802049.3309946.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/22f51641-7030-4975-92cb-ec63390b1e4f_1708306150.9546754.png)


## 2. Intuition
* Basic math: **logarithm**
* If `n` is a power of two, it has the form of $$n=2^x$$ with x is an integer. The equivalence of that would be $$x=log_2(n)$$.
<!-- Describe your first thoughts on how to solve this problem. -->

## 3. Approach
<!-- Describe your approach to solving the problem. -->
1. We can return `False` immediately if `n` doesn't satisfy the basic condition of a base 2 logarithm ($$n>0$$ of $$log_2(n)$$).
2. We calculate $$x=log_2(n)$$ and convert `x` to int.
3. Then we compute $$2^x$$ and check if it's equal to the given `n` (kind of reversing what we just did in step 2). If $$2^x=n$$ then `n` is a power of two so we return `True`, otherwise `False`.
* Follow-up: Why shouldn't we just calculate $$x=log_2(n)$$ and check if it's an integer or not? Isn't that more direct and simple than the reversing approach that we just did? Try thinking about it.
## 4. Complexity
- Time complexity: $$O(1)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 5. Code
### 5.1. Python3
```python3 []
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n > 0: return False
        x = int(log(n, 2))
        return pow(2, x) == n
```
### 5.2. C++
``` cpp []
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (!(n > 0)) {return false;}
        int x = log2(n);
        return pow(2, x) == n;
    }
};
```
### Upvote if you find this solution helpful, thank you 🤍

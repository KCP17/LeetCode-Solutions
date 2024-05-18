# 0ms - Beats 100% ✅🔥🔥🔥| Python, C++ 💻 | CONSTANT Space - SUPER EASY Solution📗

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e2b3c3a4-f3c2-44bd-8882-56be0d455491)

### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/62adfe70-cecb-466d-a39e-20bcb7f3561a_1713952550.9059045.png)

## 2. Approach

### 2.1. Algorithm: *Dynamic Programming*

### 2.2. Explanation:
1. Return the result immediately with edge cases *n = 0, 1, 2*.
2. With *n >= 3*, we need to find $$T_n$$. We'll loop `n - 2` times because if `n = 3` then we only need one iteration to add 3 of its previous numbers.
3. At each iteration:
i. We calculate the next number `T_next` in the sequence, which is the sum of first number `T_first`, middle number `T_mid`, and last number `T_last`.
ii. We also reassign first, middle, last numbers so we can move on to the next iteration to find the next `T_next` (refer to the illustration below).
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/5c39c831-efeb-4375-8808-e60c97837cef)

4. Finally, return the last calculated number `T_next`.

## 3. Code

### 3.1. Python3
```python3 []
class Solution:
    def tribonacci(self, n: int) -> int:
        match n: # Edge cases
            case 0: return 0
            case 1 | 2: return 1 # case 1 or 2
        
        T_first, T_mid, T_last = 0, 1, 1
        for i in range(n - 2):
            T_next = T_first + T_mid + T_last
            T_first, T_mid, T_last = T_mid, T_last, T_next # [0 (first), 1 (mid), 2 (last)] 3 (next) -> 0 [1 (first), 2 (mid), 3 (last)]
        return T_next
```

### 3.2. C++
```cpp []
class Solution {
public:
    int tribonacci(int n) {
        switch (n) {
            case 0:
                return 0;
            case 1:
            case 2:
                return 1;
        }
        int T_first = 0, T_mid = 1, T_last = 1;
        int T_next;
        for (int i=0; i < n-2; i++) {
            T_next = T_first + T_mid + T_last;
            T_first = T_mid, T_mid = T_last, T_last = T_next;
        }
        return T_next;
    }
};
```

## 4. Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/n-th-tribonacci-number/solutions/5066713/0ms-beats-100-python-c-constant-space-super-easy-solution) if you find this solution helpful, thank you 🤍

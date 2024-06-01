# 0ms - Beats 100% ✅🔥🔥🔥| Python, C++💻 | SUPER EASY Approach, Explanation📕

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image.png](https://assets.leetcode.com/users/images/f311fef7-e34a-4115-a27d-3e7f31d27297_1717225199.6368515.png)

### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/776fc50e-07df-4d7a-9f36-9d2a6f96a47c_1717225245.3333967.png)

## 2. Algorithms
* Simple traversing

## 3. Code
### 3.1. Python3 (with explanation each line)
```python3 []
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0 # Initialize result variable
        for i in range(len(s) - 1): # We get i & i+1 at each index so we don't need to check i as the last index but i+1
            res += abs(ord(s[i]) - ord(s[i + 1])) # `ord` to get the corresponding ASCII number of adjacent characters at i & i+1, subtract them and get the absolute value
        return res # Return the final result
```
### 3.2. C++
```cpp []
class Solution {
public:
    int scoreOfString(string s) {
        int res = 0;
        for (int i=0; i < s.size() - 1; i++) {
            res += abs(int(s[i]) - int(s[i + 1]));
        }
        return res;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/score-of-a-string/solutions/5239148/0ms-beats-100-python-c-super-easy-approach-explanation) if you find this solution helpful, thank you 🤍

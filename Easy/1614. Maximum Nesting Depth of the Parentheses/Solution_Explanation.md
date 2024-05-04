# 0ms - Beats 100% 🔥🔥🔥 | Python, C++ 💻 | Super EASY Solution - Proper explanation 📕
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C ++
![image.png](https://assets.leetcode.com/users/images/8174fc8a-2e7f-4135-a3f1-4420b632c079_1712622638.2778184.png)
### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/bdd79d34-95bc-4cc7-8bd4-37cd61565bcd_1712622155.552329.png)

## 2. Code (with explanation each line)
### 2.1. Python3
```python3 []
class Solution:
    def maxDepth(self, s: str) -> int: # Stack
        res = 0
        stack = [] # Consists of opening brackets
        for c in s:
            if c == "(":
                stack.append(c) # Push the opening bracket
            elif c == ")": # If we see a closing bracket
                res = max(res, len(stack)) # That means the number of remaining opening brackets available on stack is also the depth. We get the max depth.
                stack.pop() # Remember to pop "(" to mark finished counting a depth. E.g with "()()" if we don't pop it'll count the depth as 2.
        return res
```
### 2.2. C++
```cpp []
class Solution {
public:
    int maxDepth(string s) { // Stack
        int res = 0;
        stack<char>stack; // Consists of opening brackets
        for (char c : s) {
            if (c == '(') {
                stack.push(c); // Push the opening bracket
            }
            else if (c == ')') { // If we see a closing bracket
                res = max(res, static_cast<int>(stack.size())); // # That means the number of remaining opening brackets available on stack is also the depth. We get the max depth.
                stack.pop(); // # Remember to pop "(" to mark finished counting a depth. E.g with "()()" if we don't pop it'll count the depth as 2.
            }
        }
        return res;
    }
};
```
## 3. Complexity
- Time complexity: $$O(N)$$ since we travelled through `s` once
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$ stack
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/solutions/4995432/0ms-beats-100-python-c-super-easy-solution-proper-explanation) if you find this solution helpful, thank you 🤍

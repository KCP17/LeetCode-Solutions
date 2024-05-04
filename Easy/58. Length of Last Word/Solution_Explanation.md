# 0ms - Beats 100% 🔥🔥🔥 | Python, C++ 💻 | Super EASY Solution 📕
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++

![image.png](https://assets.leetcode.com/users/images/6cb0bace-9110-4c32-845f-deddd1b8d234_1711953574.1560886.png)
### 1.2. Python3

![image.png](https://assets.leetcode.com/users/images/a7334e9b-61a2-486d-aa2e-6c8952f33af4_1711953603.6027217.png)

## 2. Approach
<!-- Describe your approach to solving the problem. -->
Scan from the end of the string, **increment** the result if we **see** a **letter**. Otherwise, if we see a **space** and if we our **current length is > 0** that means we've **already seen a letter** before so we can **break** out of the loop and **return** the length. There're cases where we see a **space** but we **haven't seen a letter** (`res` < 0) like *example 2 in the description*, so just ignore it (don't break the loop), just keep counting.

## 3. Code
### 3.1. Python3
```python3 []
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1, -1, -1): # Start from the end & go backwards
            if s[i] != " ": # If not space
                res += 1 # Increment the length
            else: # If space
                if res > 0: # If has already checked the last word (avoid cases where there're spaces but last word is not seen yet: "   fly me   to   the moon  ")
                    break
        return res
```
### 3.2. C++
``` cpp []
class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                res++;
            }
            else {
                if (res > 0) {
                    break;
                }
            }
        }
        return res;
    }
};
```
## 4. Complexity
- Time complexity: $$O(n)$$ worst case but it's much better on average since we break as soon as we scanned through the entire last word 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote if you find this solution helpful, thank you 🤍

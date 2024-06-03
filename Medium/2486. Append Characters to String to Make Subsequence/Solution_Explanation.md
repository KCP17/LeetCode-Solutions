# Beats 94.41% ✅| Python, C++💻 | EASY Approach, Explanation📗

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/cad91f91-c5e4-4fd0-a8b1-39373e2f34f2_1717410235.7523396.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/f7e70f06-251b-4074-92cb-cfd6cd6bf373_1717413132.5040245.png)

## 2. Algorithms
* Two pointers

## 3. Code
### 3.1. Python3 (with explanation each line) 
```python3 []
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx, t_idx = 0, 0 # Starting index of both strings
        s_len, t_len = len(s), len(t) # Length of both strings
        while t_idx < t_len and s_idx < s_len: # Traverse both strings
            if s[s_idx] == t[t_idx]: # Matched characters -> confirmed this character of `t` existed in subsequence of `s`
                t_idx += 1 # Move on to next character of `t`
            s_idx += 1 # Move to next character of `s` each iteration
        # Exited the loop, `t_idx` indicates the number of confirmed characters
        return t_len - t_idx # Thus (the number of) remaining characters to be appended = total characters - confirmed characters
```
### 3.2. C++
```cpp []
class Solution {
public:
    int appendCharacters(string s, string t) {
        int s_idx = 0, t_idx = 0;
        int s_len = s.size(), t_len = t.size();
        while (t_idx < t_len && s_idx < s_len) {
            if (s[s_idx] == t[t_idx]) {
                t_idx++;
            }
            s_idx++;
        }
        return t_len - t_idx;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N)$$ length of `s`
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/solutions/5252169/beats-94-41-python-c-easy-approach-explanation) if you find this solution helpful, thank you 🤍

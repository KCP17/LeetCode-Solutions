# Beats 99.2% ✅ | Python, C++ 💻 | Easiest Approach, Clear Explanation 📕
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/c8bf4d44-10ad-45fd-8495-d1911203fe89_1707110520.8508537.png)

## 2. Approach
1. Use `Counter` method on string `s` to count the number of occurrences of each character in `s`.
2. Loop through the HashMap we just created (created with `Counter`) and check for the values. If we see a value that is equal to 1, that means its associated key (the char) only occurs 1 time, so that char is unique and therefore, we want to find its index in `s` by using `s.index(key)`. Return the value we just found.
3. If we scanned through the whole HashMap without returning the index, then there's no char with only 1 occurrence, hence no unique char and we're just going to return `-1` as the description says so.

## 3. Complexity
- Time complexity: $$O(2N)$$ with N is `s`'s length since we traverse through `s` 2 times, first is to count the occurrences and second is to find the index (`index()` function)  
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$ in the worst case if all chars in `s` are unique (memory for the HashMap).
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 4. Code
### 4.1. Python3
```python3 []
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for key, val in Counter(s).items():
            if val == 1:
                return s.index(key)
        return -1
```
### 4.2. C++
```cpp []
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int>count;
        for (char c : s) {
            count[c]++;
        }
        for (int i=0; i < s.size(); i++) {
            if (count[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```
### Upvote if you find this solution helpful, thank you 🤍

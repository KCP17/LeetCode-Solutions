# Beats 99.76% ✅🔥| Python, C++💻 | EASY Approach, Explanation📕

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image.png](https://assets.leetcode.com/users/images/1f65d95e-cec0-4dc8-b47e-af6a98755d5f_1717318697.731664.png)

### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/968c4623-2163-42cc-909f-b95a3765b7a9_1717318739.1937811.png)

## 2. Algorithms
* Two pointers

## 3. Code
### 3.1. Python3 (with explanation each line)
```python3 []
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Approach: reverse the string by swapping symmetrical characters on the left & right
        """
        l, r = 0, len(s) - 1 # Left & Right pointers initialized at both sides
        while l < r:
            tmp = s[l] # A temporary variable to hold the original value of character on the left
            s[l] = s[r] # Left character is replaced by original right character
            s[r] = tmp # Right character is replaced by original left character
            l += 1 # Move left pointer to the right
            r -= 1 # Move right pointer to the left
```
### 3.2. C++
```cpp []
class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size() - 1, tmp = 0;
        while (l < r) {
            tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l++;
            r--;
        }
    }
};
```

## 4. Complexity
- Time complexity: $$O(N/2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/reverse-string/solutions/5245581/beats-9976-python-c-easy-approach-explanation) if you find this solution helpful, thank you 🤍

# Beats 100% with 0ms ✅ | Python, C++, Ruby 💻 | Clear explanation 📗
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/6357b4e5-7c6d-45b2-84df-c07d51c976f3_1705038597.4973643.png)
### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/6fe4c8d9-22a9-41b8-8229-5c3ad436d851_1705038626.459452.png)

## 2. Approach
<!-- Describe your approach to solving the problem. -->
1. Get the index of the middle character in ``s``.
2. Loop through the left half & right half. With each iteration, checks if the lowercase of that character is in the lowercase vowels or not. If true, we increment ``count`` by 1 for the left half and decrement 1 for the right half.
3. At the end, if the amount of vowels in the left half equals to that in right half means ``count`` has been incremented the same number of times as it has been decremented, so ``count = 0`` and we return ``True`` else ``False``.

## 3. Complexity
- Time complexity: $$O(n)$$ since we loop through each character of the string.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: $$O(1)$$ ``half`` & ``count`` doesn't depend on the size of input ``s``.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 4. Code
### 4.1. Python3
```python3 []
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        count = 0
        for i in range(half):
            if s[i].lower() in 'ueoai': count += 1 # first half
            if s[i + half].lower() in 'ueoai': count -= 1 # second half
        return count == 0
```
### 4.2. C++
```cpp []
class Solution {
public:
    bool halvesAreAlike(string s) {
        int half = s.length() / 2;
        int count = 0;
        unordered_set<char>vowels = {'u', 'e', 'o', 'a', 'i'};
        for (int i=0; i < half; i++) {
            count += vowels.count(tolower(s[i]));
            count -= vowels.count(tolower(s[i + half]));
        }
        return count == 0;
    }
};
```
### 4.3. Ruby
```ruby []
def halves_are_alike(s)
    half = s.length / 2
    count = 0
    for i in 0..half-1
        count += 1 if 'ueoai'.include?(s[i].downcase)
        count -= 1 if 'ueoai'.include?(s[i + half].downcase)
    end
    return count == 0
end
```
### Upvote [here](https://leetcode.com/problems/determine-if-string-halves-are-alike/solutions/4550614/beats-100-with-0ms-python-c-ruby-clear-explanation) if you find this solution helpful, thank you 🤍

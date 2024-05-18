# Beats 97.57% ✅ | Python 💻 | Explicit explanation📕
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/4189091d-301e-4b18-ab1d-1441bf78cfda_1714558835.516316.png)

## 2. Approach
**One-pointer**

## 3. Code (Python3) - with explanation each line
```python3 []
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)): # Sequentially check the matching letter
            if word[i] == ch: # If matched
                return word[i : : -1] + word[i + 1 : ] # Return the reversed version of word from index `i` to the beginning + the remaining partition
        return word # If didn't find the matching letter then return the original `word`
```
## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$ since the returning string doesn't count towards memory
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/reverse-prefix-of-word/solutions/5095750/beats-97-57-python-explicit-explanation) if you find this solution helpful, thank you 🤍

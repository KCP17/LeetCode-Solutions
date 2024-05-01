# ONE-LINE Solution - Beats 97.52% ✅ | Python 🐍 | CLEAR EXPLANATION 📗
## Proof
![image.png](https://assets.leetcode.com/users/images/1f3de4da-38ee-4045-aa08-283ac400627e_1707280522.0048199.png)

## Approach
1. Use the `Counter` method to count the occurrences of each unique char in `s`.
2. Use the `sorted()` function to sort the unique chars *in step 1* based on their number of occurrences (the 2nd element in each key, value pair`pair[1]`). We want to sort them in descending order so `reverse = True`. Convert the dict type to list type using `.items()` because the `sorted` function only accepts list as its argument.
3. Create a list in which each element is the unique char `c` occurs `occ` times.
4. Convert that list into string using the `join` method and return it.

## Complexity
- Time complexity: $$O(N + K (log K))$$ with N length of `s` & K unique chars
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N + K)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code (Python3)
```python3 []
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([c * occ for c, occ in sorted(Counter(s).items(), key = lambda pair : pair[1], reverse = True)]) # Sort by the 2nd element (pair[1]) in each of key,val pair
```
### Upvote if you find this solution helpful, thank you 🤍

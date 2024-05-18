## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/244debc4-6d07-461c-8ec6-aae0a8c655e0)

## Code (Python)
```python []
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            N = len(w)
            r = N // 2
            l = r if N % 2 != 0 else r - 1
            while l >= 0 and w[l] == w[r]:
                if l == 0:
                    return w
                l -= 1
                r += 1
        return ""
```
## Note:
Two pointers (My solution):
- Time: O(N*(M/2)) with M length of `w` & N length of `words`
- Space: O(1)

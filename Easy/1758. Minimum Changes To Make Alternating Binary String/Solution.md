## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/d7b8d97f-d10b-4ad9-a1fc-e0d016989b76)

## Code (Python)
```python []
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        alt_str_1 = alt_str_2 = ""
        min_1 = min_2 = 0
        
        for i in range(len(s)):
            if i%2 == 0:
                alt_str_1 += "0"
                alt_str_2 += "1"
            else:
                alt_str_1 += "1"
                alt_str_2 += "0"

        for i in range(len(s)):
            if s[i] != alt_str_1[i]:
                min_1 += 1
            if s[i] != alt_str_2[i]:
                min_2 += 1

        return min(min_1, min_2)
```
## Note:
Create alternating strings & compare (my solution):
- Time: $$O(n)$$
- Space: $$O(n)$$

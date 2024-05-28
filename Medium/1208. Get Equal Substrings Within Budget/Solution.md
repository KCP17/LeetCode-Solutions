## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/ed28475a-b408-45c8-b7d1-7f8e31a0f563)

## Code
### Python3
```python []
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = 0
        cur_cost = 0
        l = 0
        for r in range(N):
            cur_cost += abs(ord(s[r]) - ord(t[r]))
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
```
### C++
```cpp []
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int N = s.size();
        int res = 0;
        int cur_cost = 0;
        int l = 0;
        for (int r=0; r < N; r++) {
            cur_cost += abs(int(s[r]) - int(t[r]));
            while (cur_cost > maxCost) {
                cur_cost -= abs(int(s[l]) - int(t[l]));
                l++;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
```
## Note:
Sliding window & Prefix sum (My solution):
- Time: $$O(2N)$$ worst case
- Space: $$O(1)$$

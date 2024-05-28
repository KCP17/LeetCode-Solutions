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

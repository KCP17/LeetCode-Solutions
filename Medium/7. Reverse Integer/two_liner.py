class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return res if -2**31 <= res <= 2**31 else 0

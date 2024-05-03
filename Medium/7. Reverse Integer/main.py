class Solution:
    def reverse(self, x: int) -> int:
        return int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) if -2**31 <= int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) <= 2**31 else 0

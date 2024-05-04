class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n > 0: return False
        x = int(log(n, 2))
        return pow(2, x) == n

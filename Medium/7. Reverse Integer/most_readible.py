class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x_reversed = int(''.join(reversed(x[1:])))
            return -x_reversed if -x_reversed >= -2**31 else 0
        else:
            x_reversed = int(''.join(reversed(x)))
            return x_reversed if x_reversed <= 2**31 else 0

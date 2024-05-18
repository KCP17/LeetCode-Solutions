class Solution:
    def pivotInteger(self, n: int) -> int: # Arithmetic Progression
        x = sqrt((n * (n + 1)) / 2)
        return int(x) if int(x) == x else -1

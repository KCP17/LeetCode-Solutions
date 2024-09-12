class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR `start` and `goal` to get all `1`s in the columns where start[i] != goal[i]
        xor = bin(start ^ goal)
        # Count the `1`s (aka the differences that need to be flipped)
        return xor.count('1')

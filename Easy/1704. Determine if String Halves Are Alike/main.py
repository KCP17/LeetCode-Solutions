class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        count = 0
        for i in range(half):
            if s[i].lower() in 'ueoai': count += 1 # first half
            if s[i + half].lower() in 'ueoai': count -= 1 # second half
        return count == 0

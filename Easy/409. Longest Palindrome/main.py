class Solution:
    def longestPalindrome(self, s: str) -> int:
        sum_even, odd = 0, False
        for freq in Counter(s).values():
            if freq % 2 == 0:
                sum_even += freq
            else:
                odd = True
                sum_even += (freq - 1)
        return sum_even + 1 if odd else sum_even

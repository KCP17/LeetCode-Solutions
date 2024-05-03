class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return True if x == ''.join(reversed(x)) else False

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0 # Initialize result variable
        for i in range(len(s) - 1): # We get i & i+1 at each index so we don't need to check i as the last index but i+1
            res += abs(ord(s[i]) - ord(s[i + 1])) # `ord` to get the corresponding ASCII number of adjacent characters at i & i+1, subtract them and get the absolute value
        return res # Return the final result

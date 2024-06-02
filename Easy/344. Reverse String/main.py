class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Approach: reverse the string by swapping symmetrical characters on the left & right
        """
        l, r = 0, len(s) - 1 # Left & Right pointers initialized at both sides
        while l < r:
            tmp = s[l] # A temporary variable to hold the original value of character on the left
            s[l] = s[r] # Left character is replaced by original right character
            s[r] = tmp # Right character is replaced by original left character
            l += 1 # Move left pointer to the right
            r -= 1 # Move right pointer to the left

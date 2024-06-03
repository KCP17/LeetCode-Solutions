class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx, t_idx = 0, 0 # Starting index of both strings
        s_len, t_len = len(s), len(t) # Length of both strings
        while t_idx < t_len and s_idx < s_len: # Traverse both strings
            if s[s_idx] == t[t_idx]: # Matched characters -> confirmed this character of `t` existed in subsequence of `s`
                t_idx += 1 # Move on to next character of `t`
            s_idx += 1 # Move to next character of `s` each iteration
        # Exited the loop, `t_idx` indicates the number of confirmed characters
        return t_len - t_idx # Thus (the number of) remaining characters to be appended = total characters - confirmed characters

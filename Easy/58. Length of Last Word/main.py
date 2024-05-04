class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1, -1, -1): # Start from the end & go backwards
            if s[i] != " ": # If not space
                res += 1 # Increment the length
            else: # If space
                if res > 0: # If has already checked the last word (avoid cases where there're spaces but last word is not seen yet: "   fly me   to   the moon  ")
                    break
        return res

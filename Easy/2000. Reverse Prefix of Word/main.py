class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)): # Sequentially check the matching letter
            if word[i] == ch: # If matched
                return word[i : : -1] + word[i + 1 : ] # Return the reversed version of word from index `i` to the beginning + the remaining partition
        return word # If didn't find the matching letter then return the original `word`

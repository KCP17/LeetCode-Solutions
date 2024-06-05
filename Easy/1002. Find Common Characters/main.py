class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # `pivot_freq` is the HashMap with common characters' frequencies to be updated after each word traversing
        # 1. Count the characters' frequencies of the first word (words[0])
        pivot_freq = Counter(words[0])
        # 2. Count the characters' frequencies of each of the remaining words, and update `pivot_freq` after each word counting
        for i in range(1, len(words)):
            cur_freq = Counter(words[i]) # The Counting HashMap of each word
            pivot_chars = list(pivot_freq.keys()) # Get all characters of `pivot_freq`
            for c in pivot_chars: # For each character of `pivot_freq`
                if c in cur_freq: # A character of `pivot_freq` also exists in `cur_freq` --> common character
                    pivot_freq[c] = min(pivot_freq[c], cur_freq[c]) # Get the smaller frequency between the two
                else: # Not a common character
                    del pivot_freq[c] # Delete it
        # 3. Append to `result` each common character a number of times that associates with its frequency
        res = []
        for c, times in pivot_freq.items(): # Get each common character along with the frequency of it
            for _ in range(times):
                res.append(c) # Append a common character a number of `times` (its frequency)
        return res

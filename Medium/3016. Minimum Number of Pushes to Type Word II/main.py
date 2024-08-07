class Solution:
    def minimumPushes(self, word: str) -> int:
        '''
        There are 8 keys which we can assign letters on each.
        Greedy is the key.
        As we want to press a minimum number of times, we need to be greedy and always assign letters in the string into the smallest-order layer of each key.
        E.g. we have word="abc", we want to assign these letters separately on different keys because then each will only take once to press and result in 3 pushes to type the whole string.
        The same idea applies to our intuition that we want the letters that are typed the most (highest frequency) to be in the lowest possible layer.
        We only move to a new layer if there are already 8 letters occupied the current layer (8 keys are all occupied).
        '''
        res = 0
        freq_map = Counter(word).most_common()
        layer = 1
        accumulated = 0
        for c, freq in freq_map:
            res += (freq * layer)
            accumulated += 1
            if accumulated == 8:
                layer += 1
                accumulated = 0
        return res

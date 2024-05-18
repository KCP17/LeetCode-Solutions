class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            N = len(w)
            r = N // 2
            l = r if N % 2 != 0 else r - 1
            while l >= 0 and w[l] == w[r]:
                if l == 0:
                    return w
                l -= 1
                r += 1
        return ""

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] == 'I':
                res += 1
                if i+1 < len(s):
                    if s[i+1] == 'V' or s[i+1] == 'X': res -=2
            elif s[i] == 'V': res += 5
            elif s[i] == 'X':
                res += 10
                if i+1 < len(s):
                    if s[i+1] == 'L' or s[i+1] == 'C': res -=20
            elif s[i] == 'L': res += 50
            elif s[i] == 'C':
                res += 100
                if i+1 < len(s):
                    if s[i+1] == 'D' or s[i+1] == 'M': res -=200
            elif s[i] == 'D': res += 500
            else: res += 1000
        return res

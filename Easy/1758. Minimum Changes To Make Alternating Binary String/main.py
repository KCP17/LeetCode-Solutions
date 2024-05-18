class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        alt_str_1 = alt_str_2 = ""
        min_1 = min_2 = 0
        
        for i in range(len(s)):
            if i%2 == 0:
                alt_str_1 += "0"
                alt_str_2 += "1"
            else:
                alt_str_1 += "1"
                alt_str_2 += "0"

        for i in range(len(s)):
            if s[i] != alt_str_1[i]:
                min_1 += 1
            if s[i] != alt_str_2[i]:
                min_2 += 1

        return min(min_1, min_2)

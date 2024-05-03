class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        output = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if (strs[j][i] if i < len(strs[j]) else "") != strs[0][i]:
                    return output

                if j == len(strs) - 1:
                    output += strs[j][i]
        return output

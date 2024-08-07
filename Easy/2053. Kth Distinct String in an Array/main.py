class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = Counter(arr)
        for s in arr:
            if freq_map[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""

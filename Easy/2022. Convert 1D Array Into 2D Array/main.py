class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: return []
        res = []
        prev = 0
        for r in range(m):
            res.append(original[prev : prev + n])
            prev += n
        return res

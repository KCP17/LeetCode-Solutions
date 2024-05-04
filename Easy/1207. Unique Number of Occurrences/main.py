class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = set()
        for occ_val in Counter(arr).values():
            if occ_val not in mem: mem.add(occ_val)
            else: return False
        return True

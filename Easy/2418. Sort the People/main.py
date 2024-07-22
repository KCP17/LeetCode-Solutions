class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip heights and names to tuples where each tuple is (heights[i], names[i])
        # Then sort based on the heights, and with reverse (descending)
        sorted_heights = sorted(zip(heights, names), reverse=True)
        # Append the names in the sorted order (2nd element of each tuple)
        res = [n for h, n in sorted_heights]
        return res

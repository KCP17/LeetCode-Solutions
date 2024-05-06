class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0 # Boats needed to use
        people.sort() # Ascending
        l, r = 0, len(people) - 1 # Left & Right pointers
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1 # Try to carry "left" if possible
            r -= 1 # Always carry "right"
            res += 1 # +1 boat used
        return res

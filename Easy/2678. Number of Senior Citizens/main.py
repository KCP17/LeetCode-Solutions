class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 1-10 (phone) --> 11 (gender) --> 12-13 (age) --> 14-15 (seat)
        res = 0
        for passenger in details:
            if int(passenger[11 : 13]) > 60: # If digits 12 & 13 (indices 11 & 12), which indicates the age
                res += 1
        return res

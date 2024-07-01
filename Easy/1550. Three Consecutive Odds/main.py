class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0 # Keep track of the number of consecutive odds
        for n in arr:
            if n % 2 != 0: # Odd (not divisible by 2) -> Increment `count`
                count += 1
                if count == 3: # Enough of consecutive odds -> True
                    return True
            else: # Even -> Even number breaks the consecutive sequence of odd numbers
                count = 0 # Reset `count`, start counting again as we see an odd number later
        return False # `count` didn't reach 3 at any point of `arr`, must be False

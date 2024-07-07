class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0 # Result
        full, empty = numBottles, 0 # current number of full and empty bottles
        while full: # Loop until we have no full bottle to drink anymore
            # 1. Drinking phase
            res += full # Drink all current full bottles
            empty += full # Those full bottles we just drank become empty, and we accumulate them to the count of empty bottles
            # 2. Exchanging phase
            exchange = empty / numExchange # Number of full bottles we can get by exchanging the current empty bottles
            full = int(exchange) # Our full bottles after we exchanged
            if exchange == full: # If `empty` is divisible by `numExchange` above, that means we can and we did exchange all our empty bottles
                empty = 0 # Thus there's no empty bottle left
            else: # Else there're some empty bottles left that are not sufficient to exchange 1 full bottle (< numExchange)
                empty -= (numExchange * full) # And those remaining empty bottles are the ones after we subtract the exchanged empty bottles from the initial empty bottles 
        return res # Return result

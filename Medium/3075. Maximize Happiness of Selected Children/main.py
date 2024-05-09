class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0 # Result
        cur_k = k # Current k after each pick
        happiness.sort() # Top of stack contains max happiness
        
        while cur_k > 0: # While budget is enough for picking (each iteration indicates each pick)
            pick = happiness.pop() # Greedy: always pick top of stack for max happiness
            picked = k - cur_k # Number of times we've picked, and also the amount of happiness to subtract from the current pick
            if pick > picked: # Ensure the current pick will still be positive after subtracting from it
                res += (pick - picked) # Add the positive subtracted happiness to result
            else: # After subtracting, if happiness is still <= 0 even though we tried to be greedy, that means there's nothing more to add to result
                break
            cur_k -= 1 # -1 turn of picking
        
        return res # Result

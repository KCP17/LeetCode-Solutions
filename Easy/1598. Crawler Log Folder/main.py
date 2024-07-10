class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0 # Result aka the moves needed to go back to main folder after all operations
        for operation in logs:
            match operation:
                case "../": # If operation is "../" -> go to parent folder -> 1 step closer to main folder
                    res -= 1 if res > 0 else 0 # Thus the needed moves decremented by 1, but only if `res` is a positive number, that means if we're not already at the main folder
                case "./": # Stay in the same folder so nothing changes, just continue
                    continue
                case _: # Any operation other than the two above will go to a child folder -> 1 step further from the main folder
                    res += 1 # Thus the needed moves incremented by 1
        return res # Return result

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # Number of rows, number of columns
        
        # 1. Flip all bits each row if the MSB (most significant bit) of that row is '0' (Greedy)
        for r in range(ROWS):
            # The left-most bit of each row is the MSB (most significant bit), its value is greater than the total value of all remaining bits in the column
            if grid[r][0] == 0: # That's why if it's '0' then we must flip it to '1', even if the remaining bits are all '1's and they're flipped to '0's after that
                for c in range(COLS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0 # If '0', flip to '1' ; If '1', flip to '0' (flip the whole row)
        
        # 2. Flip all bits each column & sum all binary numbers (represented by rows) simultaneously
        res = 0 # Initialize result variable
        for c in range(COLS):
            ones = 0 # Number of '1's in each column
            for r in range(ROWS):
                ones += grid[r][c] # Count the number of '1's in each column
            # If `ones` is less than half the number of rows that means we have more '0's than '1's in this column, but we want more '1's than '0's (Greedy)
            if ones < ROWS / 2: # So we have to flip the whole column, but we don't modify the matrix anymore, instead:
                res += (ROWS - ones) * 2**(COLS - c - 1) # We know '0's will be flipped to '1's eventually, so we accumulate `column's count of '0's` * `column's decimal value`
            else: # We've already had more '1's than '0's --> we don't flip this column
                res += ones * 2**(COLS - c - 1) # So just accumulate the result by adding `column's count of '1's` * `column's decimal value`

        return res # Result

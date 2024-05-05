class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: # Basic Grid's DFS
        def dfs(r, c, i): # Recursively search for a valid path starting from the allocated cell (by the main dfs() function)
            visited.add((r, c)) # Marked as visited
            
            if board[r][c] != word[i]: # Invalid cell -> Invalid path
                return False
            
            if i == N - 1: # If checked the last char in `word` without returning False
                return True # Once a VALID PATH is COMPLETELY FOUND, return True all the way to the main dfs() function and return True as the result
            
            if c + 1 < COLS and not (r, c + 1) in visited: # If the East adjacent cell is available & it's not been visited yet
                if dfs(r, c + 1, i + 1): # Go to that East adjacent cell, compare that East adjacent cell with the char at next index of `word`
                    return True # If COMPLETELY found a valid path then return True to the previous dfs() function -> all the way to the main dfs() function
                else:
                    visited.remove((r, c + 1)) # Else BACKTRACKING by removing that East adjacent cell from `visited` (so it can be visited again in the next path)
            
            if r + 1 < ROWS and not (r + 1, c) in visited: # Search for the South adjacent cell (Same logic as the East one)
                if dfs(r + 1, c, i + 1):
                    return True
                else:
                    visited.remove((r + 1, c))
            
            if c - 1 >= 0 and not (r, c - 1) in visited: # Search for the West adjacent cell (Same logic as the East one)
                if dfs(r, c - 1, i + 1):
                    return True
                else:
                    visited.remove((r, c - 1))
            
            if r - 1 >= 0 and not (r - 1, c) in visited: # Search for the North adjacent cell (Same logic as the East one)
                if dfs(r - 1, c, i + 1):
                    return True
                else:
                    visited.remove((r - 1, c))

        ROWS, COLS = len(board), len(board[0])
        N = len(word)
        for row in range(ROWS):
            for col in range(COLS):
                visited = set() # Avoid revisiting the visited cells in each search
                if dfs(row, col, 0): # Start a new search from every cell
                    return True # If found a valid path -> True
        return False # If started every search from every cell but still haven't found the valid path -> False

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time_per_completion = n - 1 # We need `n - 1` seconds to completely pass the pillow through the whole line (from 1 to n or n to 1)
        completed = time // time_per_completion # Count the number of lines we completed the passing of the pillow (we consider both 1 to n and n to 1)
        elapsed = time_per_completion * completed # Seconds elapsed right after we fully passed the pillow the number of `completed` lines
        remaining = time - elapsed # There's only 1 line remaining and because we cannot fully complete this line, we determine the pillow's position by counting the remaining seconds after we've fully completed as many lines as possible
        # As the 1st line goes in "1 to n" direction, if we completed an "even" number of lines, that means the line after those lines should also go in "1 to n" direction, thus the pillow's position is 1 + remaining seconds (since we start at index 1)
        # Else if we completed an "odd" number of lines, the last line should go in "n to 1" direction, that means the pillow's position is the index of person "n" - remaining seconds
        return 1 + remaining if completed % 2 == 0 else n - remaining

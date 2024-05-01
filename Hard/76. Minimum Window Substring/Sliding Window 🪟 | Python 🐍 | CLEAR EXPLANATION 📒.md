# Efficiency
![image.png](https://assets.leetcode.com/users/images/467a1421-dfa6-408d-a03a-f1ac7cc234e5_1707068041.8072896.png)

# Approach
**Sliding Window algorithm**: Create 2 pointers to identify the start and end points of the output string.
1. First, we create a HashMap `t_chars` and count the occurrences of characters of string `t` using the `Counter` method.
2. We move the left & right pointers of `s` following 2 phases:
    * 2.1. Moving right pointer: Keep the left pointer at the start of string `s` (`left = 0`). We expand the range of `s` by moving the right pointer to the right, but when to stop? The answer is when our range consists of all characters in HashMap `t_chars` (all characters in `t`) including duplicates. So how can we achieve this? We use the right pointer `right` to traverse through `s` and whenever we see a char that is in `t_chars`, we decrement its occurrence by 1. If the occurrence of a char reaches 0 that means we've moved `right`to a point where our current range includes a sufficient occurrence of that char. But that's only one char, what about the others? That is when `count = len(t_chars)` comes into play. This counts the number of unique chars in `t_chars` (ignore the occurrences). This line `if t_chars[s[right]] == 0: count -= 1` essentially says if the occurrence of char has reached 0 then we decrement the number of unique chars by 1 to indicate that we've finished searching for all occurrences of that char. If `count > 0` means we still need to move `right` further to search for the remaining occurrences (by `continue` to the next loop immediately), otherwise our range has encompassed enough of occurrences of all chars in `t` and we can move on to the next phase.
    * 2.2. Moving left pointer: This is to remove the redundant characters to minimize the length of our range. So, starting at index 0, as we move `left` to the right, if we see a char that is not in `t_chars` then that is the redundant char and we don't even need to care about it, we're just going to move the left pointer (increment `left` by 1) to leave that char out of our range. But if we see a char that is in `t_chars` then we'll have to consider whether to leave it out or not. `t_chars[s[left]] < 0` means the occurrence of a char has gone to a negative value. Well if it's negative then we must have subtracted more than enough from it in *phase 2.1*, indicating that we've not only included enough of occurrence of that char but also have included redundant occurrences. So what do we do with redundancy? We leave it out, but before we do that, we must increment the occurrence of it by 1 to say that we've left it out and out range doesn't include it anymore (the opposite of when we added it into our range in *phase 2.1* before). Else if the value is non-negative (precisely 0) then we know that our range consists of just enough occurrences of it and so we cannot leave it out since our range will be missing chars if we do that, thus we'll `break` the loop to say that "Okay stop here, don't move the left pointer any further".
3. We'll keep moving the two pointers to the end of `s`.
4. For the first time of sufficient occurrences of characters, we're just going to set `output` as the current range which our current left & right pointers determine `output == "": output = s[left : right + 1]`. For the remaining iterations, we check if the length of current range is shorter than the previous or not (`if right - left + 1 < len(output)`), if yes then assign the current range to output. By doing this, we ensure to get the shortest possible partition of `s` that includes all characters of `t`.
5. Finally, return the `output` and enjoy!

# Complexity
- Time complexity: $$O(M+N)$$ with M is the length of `t` because we used `Counter` on `t` & N is the length of `s` since we use the pointers to traverse through `s`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(K)$$ with K is the number of unique values in the HashMap `t_chars`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code (Python3)
```python3 []
class Solution:
    def minWindow(self, s: str, t: str) -> str: # Sliding Window
        if len(s) < len(t): return ""
        if t in s: return t
        t_chars = Counter(t) # Count occurrences of `t`
        count = len(t_chars) # Number of unique chars of `t`
        output = ""
        left = 0 # Left pointer
        
        for right in range(len(s)):
            if s[right] in t_chars:
                t_chars[s[right]] -= 1 # Saw the char we're searching for
                if t_chars[s[right]] == 0: # Enough occurrence of a char
                    count -= 1 # Finished searching for a char
            
            if count > 0: # Still remaining occurrences to search for
                continue
            else: # Completed searching - Sufficient
                while True:
                    if s[left] in t_chars:
                        if t_chars[s[left]] < 0: # Redundancy
                            t_chars[s[left]] += 1 # Leave out
                        else:
                            break # Don't leave out
                    left += 1 # Reduce the range
                
                if right - left + 1 < len(output) or output == "": # Minimize
                    output = s[left : right + 1]
        
        return output
```
## Upvote if you find this solution helpful, thank you 🤍

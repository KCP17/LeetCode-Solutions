# Beats 99.25% ✅🔥🔥| Python💻 | EASY, STEP BY STEP Explanation📒

## 1. Proof (Python3)
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/a220324d-8d8c-49ab-a411-a5a5f9dd5bd6_1716605939.655781.png)

## 2. Algorithms
* Hash Set
* Backtracking

## 3. Code (with explanation each line)
```python3 []
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(i, cur_word, cur_sentence):
            '''
            At each index, decide to space if valid, and always inspect the case where we don't space
            i: index of current character -> s[i]
            cur_word: current word that we're assessing -> if finished assessing a valid word (in wordDict) then `cur_word` resets to an empty string ""
            cur_sentence: current sentence we're assessing -> if valid then we'll subsequently add to the result array
            '''
            if i == N: # Base case: reached the end of `s`
                removed_white_spaces = cur_sentence.replace(" ", "")
                if len(removed_white_spaces) == N: # A valid sentence should have the same length (excluding white spaces) as `s`
                    self.res.append(cur_sentence.strip()) # Removing the redundant space at the end from the previous call
                return # Reached the end, nothing more to inspect, just return
            
            # Decision to space or not
            cur_word += s[i] # Add the current character s[i] to current word
            if cur_word in wordDict: # If we've completed a valid word (in wordDict)
                # Then assess a new word by going to next char s[i+1], with `cur_word` reset at "", update the current sentence to include assessed word & a space " "
                backtrack(i + 1, "", cur_sentence + cur_word + " ")
            # Always inspect the case where we don't space despite the decision above, it may lead to a different sentence even if the assessed word is valid (in wordDict)
            backtrack(i + 1, cur_word, cur_sentence)

        N = len(s)
        wordDict = set(wordDict) # Convert to set for constant time lookup
        self.res = [] # Result array
        backtrack(0, "", "") # Start searching & backtracking at index 0, with current word & current string all empty
        return self.res # Return final result
```

## 4. Complexity
- Time complexity: $$O(2^N)$$ worst case
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$ length of `cur_sentence`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/word-break-ii/solutions/5204047/beats-99-25-python-easy-step-by-step-explanation) if you find this solution helpful, thank you 🤍

## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/8d87b2a7-5418-4fc1-a774-d1394dc79cbe)

## Code (Python3) - Along with explanation each line
```python3 []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [[strs[0]]]
        HashMap = {}
        output = []
        index = 0
        for string in strs:
            seen = frozenset(Counter(string).items()) # Check anagrams since the order doesn't matter {'t','e','a'} == {'a','t','e'} - Counter cuz occurrences matter
            if seen in HashMap: # frozenset is immutable therefore can be hashed
                output[HashMap[seen]].append(string) # Append the anagram right in the subset of allocated index
            else: # Only execute when encounter a new type of anagram
                output.append([string]) # New, different anagram, just append
                HashMap[seen] = index # Save the cur anagram and allocate the index so its anagrams know which subset to append as above
                index += 1 # Move onto the next type of anagram
        return output
```
## Note:
Logic (My solution):
- Time: $$O(n * k)$$ with n is the length of strs & k is length of each string
- Space: $$O(n)$$ HashMap

# Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/c4d1d6d7-b0eb-42d8-b1b1-e0add7883952_1705210727.779218.png)
![image.png](https://assets.leetcode.com/users/images/5edadb4b-4a0f-4961-8bbd-065fe7ae48f4_1705210778.2718132.png)

# Illustration
![Determine if 2 strings are close.jpg](https://assets.leetcode.com/users/images/4e859429-a928-4730-92e9-e242a962fc34_1705212855.6235945.jpeg)
## Explanation
1. To turn a given string into another given string, we must guarantee that these two strings have the same characters.
2. We also need the characters of these strings to have the same occurrences. To make this easier to understand, first let's modify two strings so that the same characters are contiguous because we're allowed to do this, right? We're allowed to swap the characters (e.g ``word1`` in the illustration: ``cabbba`` -> ``caabbb`` and because ``word2`` is already modified in contiguous order we don't need to modify it anymore). Subsequently, we can transform all occurrences of a type of character into another type, and we do that on one of the two strings to match the other. We have ``word1 = caabbb`` & ``word2 = abbccc``, we can see the order of occurrences of two strings matched together (1, 2, 3 respectively). Even if they don't match in order but as long as they have the same occurrences then it can also work (because we can always swap them, right?). Thus, we can turn ``word1`` into ``word2`` by transforming ``c`` to ``a``, all ``a``s to ``b``s, and all ``b``s to ``c``s.
3. Therefore, we have to check 2 things: two strings have the same characters, and have the same characters' occurrences.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Edge cases: return ``False`` if the length of ``word1`` & ``word2`` are not the same. Return ``True`` if two given strings are empty (in the first line we've already compared the length of these strings, if the program still runs to the second line that means these strings have the same length, therefore we only need to check if ``word1``'s length = 0). Another case we can return ``True`` is that two strings are exactly the same.
2. We used the pre-built ``Counter`` method to track the occurrences of unique characters in ``word1`` & ``word2``.
3. Return ``True`` if the unique characters of two strings are the same **AND** the numbers of occurrences of the characters are the same (sorted to ensure the order), else ``False``.

# Complexity
- $$n$$ is the length of string, $$k$$ is the length of unique characters.
- Time complexity: $$O(n + k(logk))$$ because the ``Counter`` method takes linear time and the ``sorted`` method takes quasilinear time on unique characters of both strings.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(k)$$ - used for storing unique characters & their occurrences.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
## Python3
```python3 []
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        if len(word1) == 0 or word1 == word2: return True
        occ1 = Counter(word1) # Track occurrences of word1
        occ2 = Counter(word2) # Track occurrences of word2
        return occ1.keys() == occ2.keys() and sorted(occ1.values()) == sorted(occ2.values()) # If same characters & same number of occurrences
```
## C++
```cpp []
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) {return false;}
        if (word1.length() == 0 || word1 == word2) {return true;}
        
        unordered_map<char,int>occ1, occ2;
        vector<char>keys1, keys2;
        vector<int>vals1, vals2;
        
        for (int i=0; i < word1.length(); i++) {
            occ1[word1[i]]++;
            occ2[word2[i]]++;
        }
        
        for (auto it = occ1.begin(); it != occ1.end(); ++it) {
            keys1.push_back(it->first);
            vals1.push_back(it->second);
        }
        for (auto it = occ2.begin(); it != occ2.end(); ++it) {
            keys2.push_back(it->first);
            vals2.push_back(it->second);
        }
        
        sort(keys1.begin(), keys1.end()); sort(keys2.begin(), keys2.end());
        sort(vals1.begin(), vals1.end()); sort(vals2.begin(), vals2.end());
        return keys1 == keys2 && vals1 == vals2;
    }
};
```
## Ruby
```ruby []
def close_strings(word1, word2)
    return false if word1.length != word2.length
    return true if word1.length == 0 || word1 == word2
    occ1 = word1.chars.tally
    occ2 = word2.chars.tally
    return occ1.keys.sort == occ2.keys.sort && occ1.values.sort == occ2.values.sort
end
```
## Upvote if you find this solution helpful, thank you 🤍

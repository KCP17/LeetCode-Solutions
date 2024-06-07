## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/04e4e5f3-05d6-48ec-a043-e0c881fff642)

## Code (Python3)
```python3 []
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        new_sent = []
        cur_word = ""
        for c in sentence:
            if c is not " ":
                if cur_word in dictionary: # Found a root
                    continue
                cur_word += c
            else:
                new_sent.append(cur_word)
                new_sent.append(" ")
                cur_word = ""
        new_sent.append(cur_word)
        return "".join(new_sent)
```
## Time & Space:
HashSet (My solution):
- Time: $$O(d + 2n)$$ with d=len(dict), n=len(sentence)
- Space: $$O(w + n)$$ with w=len(each_word)

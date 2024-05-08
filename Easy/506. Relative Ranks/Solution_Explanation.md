# Beats 93.52%✅| Easy Approach📗| Python💻

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/fde72cba-635b-4d19-b281-e02879343f07_1715161288.189072.png)

## 2. Algorithms
- Sorting

## 3. Code (Python3) - with explanation
```python3 []
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = []
        ans = [None] * len(score)
        
        # For each pair: pair[0] is the athlete, pair[1] is the corresponding score
        for i, s in enumerate(score):
            pairs.append((i, s))
        
        # Sort the pairs in decreasing scores order (p[1])
        pairs.sort(key=lambda pair : pair[1], reverse=True)
        
        # Assign the award for each athlete
        for rank, pair in enumerate(pairs):
            match rank:
                case 0:
                    ans[pair[0]] = "Gold Medal"
                case 1:
                    ans[pair[0]] = "Silver Medal"
                case 2:
                    ans[pair[0]] = "Bronze Medal"
                case _: # Other rankings
                    ans[pair[0]] = str(rank + 1)

        return ans
```

## 4. Complexity
- Time complexity: $$O(3N + N*log(N))$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/relative-ranks/solutions/5129517/beats-93-52-easiest-approach-python) if you find this solution helpful, thank you 🤍

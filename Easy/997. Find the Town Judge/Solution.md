## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/2e97dcf0-be5d-41cb-8980-5644308c3b1d)

## Code (Python3)
```python3 []
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return n # If there's 1 person then that's the judge
        elif len(trust) == 1: return trust[0][1]
        hashMap = defaultdict(set) # Key: the person who's trusted, value: the people who trust that person
        judge = 0
        
        for pair in trust:
            hashMap[pair[1]].add(pair[0])
        
        for trusted in hashMap.keys():
            if len(hashMap[trusted]) == n - 1:
                for trusts in hashMap.values():
                    if trusted in trusts:
                        judge = -1
                        break
                
                if judge == -1:
                    judge = 0
                    continue
                else:
                    return trusted
        return -1
```
## Note:
HashMap (My solution):
- Time: $$O(T + N^2)$$ with T length of `trust` & N number of people
- Space: $$O(T)$$

## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/6e9a8ea7-f448-470a-a53f-34c167211462)

## Code (Python3)
```python3 []
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([n for n in range(1, n + 1)])
        while len(q) > 1:
            for count in range(1, k + 1):
                n = q.popleft()
                if count != k:
                    q.append(n)
        return q[-1]
```

## Note:
Queue (My solution):
- Time: $$O(n * k)$$
- Space: $$O(n)$$

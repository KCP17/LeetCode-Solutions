## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/98a3eec8-d38f-49d2-9bfb-d8246f4723d0)

## Code (Python3)
```python3 []
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res
```
## Note:
Normal sorting (My solution):
- Time: $$O(2 * n * log(n))$$
- Space: $$O(1)$$

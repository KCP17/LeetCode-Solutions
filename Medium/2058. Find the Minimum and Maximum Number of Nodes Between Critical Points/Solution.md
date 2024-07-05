## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/25f7b6c3-9345-4fff-a15c-98d90d741d30)

## Code
### Python3
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDist, maxDist = float('inf'), 0
        prev = head
        cur = head.next
        i = 0
        first_CritNode, prev_CritNode = None, None
        while cur.next:
            if (cur.val < prev.val and cur.val < cur.next.val) or (cur.val > prev.val and cur.val > cur.next.val): # Confirmed critical point
                if first_CritNode is None:
                    first_CritNode = i
                else:
                    minDist = min(minDist, i - prev_CritNode)
                    maxDist = max(maxDist, i - first_CritNode)
                prev_CritNode = i

            prev = cur
            cur = cur.next
            i += 1
        
        return [minDist, maxDist] if maxDist > 0 else [-1, -1]
```

## Note:
[ Time taken: 16 m 1 s ]
- Time: O(n)
- Space: O(1)

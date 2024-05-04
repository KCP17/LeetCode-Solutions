## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/85accbca-e21d-4d90-946f-b73b6e2e2bfd)

## Code (Python3)
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rec(cur):
            if not cur: return
            forward.append(cur.val)
            rec(cur.next)
            backward.append(cur.val)
            return
        
        forward, backward = [], []
        rec(head)
        return forward == backward
```
## Note:
Recursion (My solution - follow-up requirements unsatisfied):
- Time: $$O(3N)$$
- Space: $$O(3N)$$ with 2 lists & a stack

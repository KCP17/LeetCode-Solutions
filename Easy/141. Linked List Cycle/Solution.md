## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/c0c96c7d-3c02-4f2a-8300-c0e25a37822c)

## Code (Python3)
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head: # Travel through each node from head
            if head in seen: # If current node has already been in `seen` -> Cycle
                return True
            seen.add(head) # Add current node to `seen` to indicate we've seen it
            head = head.next # Replace current node with its next node for the next loop
        return False # If hasn't returned True (above) means no cycle
```
## Time & Space:
* Time: $$O(N)$$
* Space: $$O(N)$$ doesn't satisfy follow-up requirements

## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/a50116f6-5a1e-40a8-8aea-1fc4b89a4f38)

## Code (Python3)
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]: # Monotonic stack
        mono_stack = []
        node = head
        
        while node:
            while mono_stack and mono_stack[-1].val < node.val:
                mono_stack.pop()
            
            if mono_stack:
                mono_stack[-1].next = node
            else:
                head = node
            
            mono_stack.append(node)
            node = node.next
        
        return head
```
## Note:
Monotonic stack (My solution):
- Time: $$O(2N)$$
- Space: $$O(N)$$

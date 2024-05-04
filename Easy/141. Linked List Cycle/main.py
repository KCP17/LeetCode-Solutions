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

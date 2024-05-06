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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        size = 0
        while node: # Count the size of linked list
            size += 1
            node = node.next
        
        mid = size // 2 # Find the middle index
        
        while mid > 0: # Loop till the middle index
            mid -= 1
            head = head.next # Sequentially moving through the linked list
        
        return head

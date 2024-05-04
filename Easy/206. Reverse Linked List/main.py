# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Recursion
        def rec(prev, cur):
            if not cur: # If `cur` is out of range (too far to the right)
                return None
            
            head = rec(cur, cur.next) # Recursively find the last node
            
            if not cur.next: # If `cur` is the last node in list
                head = cur # Then it's also the new head
            
            cur.next = prev # Reverse the pointer. The previous recursive function called this function with `prev` as the cur node of that prev recursive func
            return head
        
        return rec(None, head)

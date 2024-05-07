# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        co = prev = ListNode(0, head)
        cur = head
        
        while cur:
            db = cur.val * 2
            if db > 9:
                cur.val = db - 10
                prev.val += 1
            else:
                cur.val = db
            
            prev = cur
            cur = cur.next
        
        return head if co.val == 0 else co

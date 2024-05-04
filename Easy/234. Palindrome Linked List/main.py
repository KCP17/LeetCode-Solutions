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

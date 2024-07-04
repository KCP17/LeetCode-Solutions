# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dst = head
        node = head.next
        num = 0
        while node:
            if node.val == 0:
                dst.val = num
                num = 0
                if node.next:
                    dst.next = node
                    dst = node
                else:
                    dst.next = None
            else:
                num += node.val

            node = node.next
        
        return head

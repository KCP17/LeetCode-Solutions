# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.size = 0
        def find_size(node):
            if not node:
                return self.size
            self.size += 1
            find_size(node.next)
        
        def remove(node, step):
            if step == 0:
                if self.steps + 2 == self.size:
                    node.next = None
                else:
                    node.next = node.next.next
                return
            remove(node.next, step - 1)
        
        find_size(head)
        
        self.steps = self.size - n - 1
        
        if self.steps < 0:
            return head.next
        
        remove(head, self.steps)
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Reverse the pointers from the middle to the end (see Leetcode 234)
        ## 1.1. Identify the mid (`slow` ptr)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ## 1.2. Reverse the pointers from mid -> end
        prev = None
        while slow:
            ori_nxt = slow.next
            slow.next = prev
            prev = slow
            slow = ori_nxt
        
        # 2. Reorder the list (refer to Visualization.png)
        last_node = ListNode(0, head)
        cur_left = head # First node (left-most)
        cur_right = prev # Last node (right-most)
        while cur_left and cur_right: # Go from both ends to the middle
            ori_nxt_left = cur_left.next
            ori_nxt_right = cur_right.next

            last_node.next = cur_left
            last_node = cur_left.next = cur_right

            cur_left = ori_nxt_left
            cur_right = ori_nxt_right
            if cur_left == cur_right:
                last_node.next = cur_left
                break

# Beats 98.44%✅ | CONSTANT Space🔥| Explicit VIDEO Explanation + Visualization + Simulation📙 | Python💻

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/89d8e225-aab5-4104-be8f-7e8db8db2a58_1715061117.703333.png)

## 2. Algorithms
- Math

## 3. Explanation
_Click on this image to watch my YouTube explanation video_
[![Click on this image to watch the YouTube explanation video](https://i.ytimg.com/vi/9_y37-o6W5A/maxresdefault.jpg)](https://youtu.be/9_y37-o6W5A?si=na24Y5sQvIwnIRyS)

## 4. Code (Python3)
```python3 []
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
```

## 5. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/solutions/5123907/beats-98-44-constant-space-explicit-video-explanation-visualization-simulation-python) if you find this solution helpful, thank you 🤍

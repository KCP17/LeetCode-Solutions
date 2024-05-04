class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: # Monotonic stack
        ans = []
        mono_stack = [] # Decreasing
        nxt_grt = {}
        
        for i in range(len(nums2) - 1, -1, -1):
            while mono_stack and mono_stack[-1] <= nums2[i]:
                mono_stack.pop()
            
            nxt_grt[nums2[i]] = mono_stack[-1] if mono_stack else -1
            
            mono_stack.append(nums2[i])
        
        for i in range(len(nums1)):
            ans.append(nxt_grt[nums1[i]])
        
        return ans

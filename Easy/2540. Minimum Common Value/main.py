class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int: # Two pointers
        pt1, pt2 = 0, 0 # pointer 1 of nums1, pointer 2 of nums2
        while not pt1 == len(nums1) and not pt2 == len(nums2): # loop while both pointers are in range
            if nums1[pt1] == nums2[pt2]: # Found the smallest common value
                return nums1[pt1] # Return that value
            elif nums1[pt1] < nums2[pt2]: # Value in nums1 is too small compared to value in nums2
                pt1 += 1 # Move to the right for it to become bigger
            else: # Value in nums2 is too small compared to value in nums1
                pt2 += 1
        return -1 # Exited the loop means 1/2 or both pointers go out of range -> no common value

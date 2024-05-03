class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype - type of return value: List[int]

        Iterates through each number in the list
        With each number, find x so that: current_num + x = target
        """
        # current + x = target
        for i in range(len(nums)): # Iterate through each number
            x = target - nums[i] # x is the number to find
            # If x exists in the list and its index is not the index of current_num
            if x in nums and nums.index(x) != i: # Index_of_x = nums.index(x)
                return [i, nums.index(x)] # Return index of current_num & index of x

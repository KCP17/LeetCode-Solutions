class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        for i in range(N):
            x = N - i # The number of elements on the right and including current, and possibly the result `x` up to this `i` index if this `x` is valid
            # Check for validity
            # nums[i] >= x: There're 'x' elements on the right & current, so if `current >= x` that means there're `x` numbers on the right & current greater than `x` (sorted array)
            # max_of_left: max number on the left - we need to make sure there's no number greater than `x` on the left, thus `x > greatest_num_on_the_left` (sorted array)
            max_of_left = nums[i - 1] if i - 1 >= 0 else 0
            if nums[i] >= x and x > max_of_left:
                return x
        return -1

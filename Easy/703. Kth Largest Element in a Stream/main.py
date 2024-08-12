class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val: int) -> int:
        i = bisect_left(self.nums, val)
        self.nums.insert(i, val)
        return self.nums[len(self.nums) - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

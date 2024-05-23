class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i):
            if i == len(nums):
                if self.avoid:
                    self.res += 1
                return

            # Numbers to avoid
            avoid_1 = nums[i] - k
            avoid_2 = nums[i] + k
            
            # ONLY include IF current number doesn't need to be avoided
            if nums[i] not in self.avoid:
                self.avoid[avoid_1] += 1
                self.avoid[avoid_2] += 1
                dfs(i + 1)
            
                # Not include
                self.avoid[avoid_1] -= 1
                self.avoid[avoid_2] -= 1
                if self.avoid[avoid_1] <= 0:
                    del self.avoid[avoid_1]
                if self.avoid[avoid_2] <= 0:
                    del self.avoid[avoid_2]
            dfs(i + 1)

        self.res = 0
        self.avoid = defaultdict(int)
        dfs(0)
        return self.res

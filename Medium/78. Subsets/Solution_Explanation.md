## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/bfb4a223-ce53-4569-92b8-d1f9280d45a9)

## Code (Python3) - with succinct explanation
```python3 []
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, include):
            if i == len(nums): # Base case: out of range
                return
            
            if include: # Include current number if was directed by the call of the parent dfs()
                self.subsets[-1].append(nums[i])
            
            dfs(i + 1, True) # Include next number
            dfs(i + 1, False) # Not include next number
            self.subsets.append(self.subsets[-1].copy()) # Fixed the current path & move on to the new path (*)
            
            if self.subsets[-1] and nums[i] == self.subsets[-1][-1]: # Backtracking if top of new path is the same as current indexed number
                self.subsets[-1].pop()
            else: # Else remove the entire new path. This won't cause missing path as this removed path is just the copy of the fixed old path, as written in line (*) above
                self.subsets.pop()
            return
        
        self.subsets = [[]]
        dfs(0, True) # Include nums[0]
        self.subsets.append([])
        dfs(0, False) # Not include nums[0]
        self.subsets.pop() # Remove redundant blank path 
        return self.subsets
```
## Note:
DFS + Backtracking (My solution):
- Time: $$\sum_{k=1}^{n} k * C^k_n$$ with k from 0 to n
- Space: $$O(n)$$ recursive call stacks

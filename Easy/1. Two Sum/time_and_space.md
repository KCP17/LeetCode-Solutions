## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/102e9ebe-703d-41e9-a6fe-fcccd5345d44)

## Code (Python)
```python []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype - type of return value: List[int]

        Iterates through each number in the list
        With each number, find x so that: current_num + x = target
        """
        #current + x = target
        for i in range(len(nums)): #iterate through each number
            x = target - nums[i] #x is the number to find
            #if x exists in the list and its index is not the index of current_num
            if x in nums and nums.index(x) != i: #index_of_x = nums.index(x)
                return [i, nums.index(x)] #return index of current_num & index of x
```
## Time & Space:
* Time: $$O(n^2)$$
* Space: $$O(1)$$

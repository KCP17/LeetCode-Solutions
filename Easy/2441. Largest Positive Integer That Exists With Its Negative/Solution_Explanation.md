# Beats 99.07% Time⌛ 98.70% Memory 💾🔥🔥 | Python, C++ 💻 | Clear Explanation📗
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/11bf8ec1-ba8b-418f-9ae2-4a5d23b5702c_1714622105.9590352.png)
### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/4501ad22-9d9b-42cd-916c-b402ca4554e6_1714623094.1484709.png)

## 2. Approach
**Sorting** & **Two pointers**

## 3. Code
### 3.1. Python3 (with explanation each line)
```python3 []
class Solution:
    def findMaxK(self, nums: List[int]) -> int: # Two pointers
        nums.sort() # Negative integer with max abs value (|-|) on the left, whereas the max positive integer (+) on the right
        l, r = 0, len(nums) - 1 # left & right pointers -> We go from both ends to inside to get the max value
        
        while nums[l] < 0 and nums[r] > 0: # Ensure the left pointer always points to a negative integer (-) & right pointer always points to a positive integer (+)
            neg, pos = abs(nums[l]), nums[r] # Get the absolute value of negative number (-), and positive number (+) -> for easier comparison
            if neg == pos: # If abs of negative (|-|) matches positive (+) -> Found
                return pos # Return the positive (+) number
            elif neg < pos: # The positive number (+) is too large compared to the corresponding abs of negative number (|-|) which left pointer is pointing at
                r -= 1 # Get a smaller positive number (+) by moving right pointer inside
            else: # The abs of negative number (|-|) is too large compared to the corresponding positive number (+) which right pointer is pointing at
                l += 1 # Get a smaller abs of negative number (|-|) by moving left pointer inside
        
        return -1 # Not found
```
### 3.2. C++
```cpp []
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;

        while ((nums[l] < 0) && (nums[r] > 0)) {
            int neg = abs(nums[l]), pos = nums[r];
            if (neg == pos) {
                return pos;
            }
            else if (neg < pos) {
                r--;
            }
            else {
                l++;
            }
        }
        return -1;
    }
};
```
## 4. Complexity
- Time complexity: $$O((N*logN) + N/2)$$ simplified to $$O(N*logN)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/solutions/5099232/beats-99-07-time-98-70-memory-python-c-clear-explanation) if you find this solution helpful, thank you 🤍

# Beats 94.87% ✅| Python, C++ 💻 | Easiest approach with Clear Explanation 📗

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/af5a722e-d991-41f8-9a23-12ab8a4dbc8a_1709944924.1075964.png)

## 2. Approach - Explanation
<!-- Describe your approach to solving the problem. -->
#### **Two pointers** approach
1. Initialize `pt1` (pointer 1) that refers to the index of `nums1`, `pt2` (pointer 2) refers to the index of `nums2`. Initially, they're all 0 (beginning of each list).
2. At each iteration, we check if the element of `pt1` and element of `pt2` are the same so we can return that element. If not, we move the index of the smaller element by 1 to the right.
3. The process repeats until one of the two pointers go out of range. Till this point, we know that there can't be any common value between `nums1` & `nums2`, let alone the smallest common element. Therefore, we return `-1`.
* Note that 2 lists are sorted in non-decreasing order, or we can say they're nearly in increasing order, and we start from the left-most position of those lists then move to the right (start from the smallest value). We stop as soon as we found the same value between them and that value must be the smallest common value.

## 3. Complexity
- Time complexity: $$O(N + M)$$ with N, M are the sizes of 2 lists
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 4. Code
### 4.1. Python3
```python3 []
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
```

### 4.2. C++
```cpp []
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int pt1 = 0, pt2 = 0;
        while (!(pt1 == nums1.size()) && !(pt2 == nums2.size())) {
            if (nums1[pt1] == nums2[pt2]) {
                return nums1[pt1];
            }
            else if (nums1[pt1] < nums2[pt2]) {
                pt1++; 
            }
            else {
                pt2++;
            }
        }
        return -1;
    }
};
```

### Upvote [here](https://leetcode.com/problems/minimum-common-value/solutions/4845219/beats-94-87-python-c-easiest-approach-with-clear-explanation) if you find this solution helpful, thank you 🤍

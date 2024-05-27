# 0ms - Beats 100% ✅🔥🔥🔥| Python, C++💻 | EASY, CLEAR Explanation📗

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image.png](https://assets.leetcode.com/users/images/b23d62b2-cd69-4556-aaea-8fda460dcc05_1716793681.114781.png)

### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/ff8a9a5f-7755-4d41-aba0-273a88311a22_1716793224.750583.png)

## 2. Algorithms
* Sorting

## 3. Code

### 3.1. Python3 (with explanation each line)
```python3 []
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
```

### 3.2. C++
```cpp []
class Solution {
public:
    int specialArray(vector<int>& nums) {
        int N = nums.size();
        sort(nums.begin(), nums.end());
        int x, max_of_left;
        for (int i=0; i < N; i++) {
            x = N - i;
            max_of_left = (i - 1 >= 0) ? nums[i - 1] : 0;
            if ((nums[i] >= x) && (x > max_of_left)) {
                return x;
            }
        }
        return -1;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N + Nlog(N))$$ sorting & array traversing
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/solutions/5214817/0ms-beats-100-python-c-easy-clear-explanation) if you find this solution helpful, thank you 🤍

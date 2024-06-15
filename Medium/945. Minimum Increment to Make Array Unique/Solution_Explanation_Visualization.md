# Beats 100% With Python3🔥🔥🔥✅| VIDEO Explanation + Visualization + Simulation📙| Python, C++💻

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/ebf0fe12-11eb-47e9-80e1-78c4f44cd7d7_1718456324.3287055.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/d1aeda71-e7dd-4821-981d-30ebf54209c4_1718456361.284057.png)

## 2. Algorithms
- Counting Sort
- Greedy
- Arithmetic Progression (Math)

## 3. Explanation
_Click on this image to watch my YouTube explanation video_
[![Click on this image to watch the YouTube explanation video](https://i.ytimg.com/vi/rc-p2qd25N8/maxresdefault.jpg)](https://youtu.be/rc-p2qd25N8?si=q85tRQ0QoogUTyrt)

## 4. Code

### 4.1. Python3
```python3 []
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 1. Counting (bucket) sort
        max_index = max(nums) + 1
        nums_cnt = [0] * max_index
        for n in nums:
            nums_cnt[n] += 1
        
        # 2. Count the moves
        res = 0
        carry = 0
        for occ in nums_cnt:
            res += carry
            if occ == 0:
                if carry > 0:
                    carry -= 1
            else:
                carry += (occ - 1)
        
        # 3. Add remaining moves
        if carry > 0:
            res += ((1 + carry) * (carry / 2))
        
        # 4. Return result
        return int(res)
```

### 4.2. C++
```cpp []
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        // 1. Counting (bucket) sort
        int max_index = *max_element(nums.begin(), nums.end()) + 1;
        vector<int> nums_cnt(max_index, 0);
        for (int n : nums) {
            nums_cnt[n]++;
        }

        // 2. Count the moves
        int res = 0;
        int carry = 0;
        for (int occ : nums_cnt) {
            res += carry;
            if (occ == 0) {
                if (carry > 0) {
                    carry--;
                }
            }
            else {
                carry += (occ - 1);
            }
        }
        
        // 3. Add remaining moves
        if (carry > 0) {
            res += ((1 + carry) * (carry / 2.0));
        }

        // 4. Return result
        return int(res);
    }
};
```

## 5. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(M)$$ with `M = max(nums) + 1`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/minimum-increment-to-make-array-unique/solutions/5317531/beats-100-with-python3-video-explanation-visualization-simulation-python-c) if you find this solution helpful, thank you 🤍

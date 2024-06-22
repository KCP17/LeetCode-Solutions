# Beats 99.25%✅🔥🔥| Python, C++💻 | CLEAR Explanation📙

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/4e18539d-0713-4d11-91a6-7ea2130f0a9d_1719075044.3910954.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/8e2af393-2780-4e60-bcfc-7ed3b7201bd8_1719075175.8163018.png)

## 2. Algorithms
* One pointer

## 3. Code

### 3.1. Python3 (with inline explanation & simulation)
```python3 []
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''----READ THE CODE FIRST, THEN READ THIS SIMULATION----
        E.g [2,2,1,1,2,1,2,2,2,1], k = 3
             0 1 2 3 4 5 6 7 8 9 (indices)
        When i = 5, we accumulated 3 odds (=k) for the first time, `odds = [2,3,5]`, we know there're 3 subarrays ending at i = 5
        [2,2,1,1,2,1] (subarr 1) - starting from next of `removed = -1`
          [2,1,1,2,1] (subarr 2)
            [1,1,2,1] (subarr 3) - starting from index of oldest odd (`odds[oldest]`)
         0 1 2 3 4 5 (indices)
        ==> `res` increased by (oldest_odd_index - removed) = (2 - (-1)) = 3 --> res += 3 (1)
        Same happens when we get to indices 6,7,8 as the number of odds is still 3 which matches `k`, our `removed` & `oldest` are still the same
        Thus with 3 times (6,7,8) of increasing by 3 each time (just like when i=5)
        ==> `res` increased by 3*3 = 9 --> res += 9 (2)
        When i=9, we add another odd number -> exceeded `k=3`
        -> we have to set the oldest odd to be the removed odd -> `removed = 2`
        -> Our "new" oldest odd is the next one of the removed odd -> move pointer `oldest += 1` -> pointer `oldest = 1` -> odds[oldest] = 3
        Now, `odds = [2(removed),3(odds[oldest]),5,9]`
        --> We start counting new subarrays starting from the next index of the one we just removed, we only have 1 more subarray in this case:
                 [1,2,1,2,2,2,1]
            0 1 2 3 4 5 6 7 8 9 (indices)
        ==> `res` increased by 3 - 2 = 1 --> res += 1 (3)
        From (1), (2), (3) --> Our final result = 3 + 9 + 1 = 13
        '''
        res = 0 # Result
        odds, amount = [], 0 # Array to store indices of odd numbers, and its current amount of odds (different from length as we may remove some odds in `odds` without changing its length)
        removed, oldest = -1, 0 # The removed odd number, and the pointer of the oldest odd number in `odds`
        N = len(nums)
        
        for i in range(N): # Loop through each index
            if nums[i] % 2 != 0: # If encounter an odd number
                odds.append(i) # Append its index to the right of odd numbers queue
                amount += 1 # Increment the number of odds
            
            if amount > k: # If exceeded the limit `k` of odd numbers
                removed = odds[oldest] # The oldest odd number is removed (to keep exactly `k` odds), also we'll start counting our subarrays from there
                oldest += 1 # Our oldest existed odd is now the next of the one we just removed
                amount -= 1 # Decrement the number of odds (because we just removed 1)
            
            if amount == k: # Matched `k` odd numbers
                # The number of subarrays increased is the number of subarrays starting from the next index of the removed odd up to starting from the oldest odd, and ending at current `i`
                # At first, we instantiate our `removed = -1` dictates that we start counting our subarrays from next index of -1, which is 0
                res += (odds[oldest] - removed)
        
        return res
```

### 3.2. C++
```cpp []
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int res = 0;
        vector<int>odds;
        int amount = 0, removed = -1, oldest = 0;
        int N = nums.size();
        for (int i=0; i<N; i++) {
            if (nums[i] % 2 != 0) {
                odds.push_back(i);
                amount++;
            }
            if (amount > k) {
                removed = odds[oldest];
                oldest++;
                amount--;
            }
            if (amount == k) {
                res += (odds[oldest] - removed);
            }
        }
        return res;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(M)$$ with `M` odd numbers in `nums`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/count-number-of-nice-subarrays/solutions/5353443/beats-99-25-python-c-clear-explanation) if you find this solution helpful, thank you 🤍

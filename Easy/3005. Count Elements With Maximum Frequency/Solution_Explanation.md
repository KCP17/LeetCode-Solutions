# 0ms - Beats 100% 🔥🔥🔥 | Python, C++ 💻
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C++
![image.png](https://assets.leetcode.com/users/images/51ea8c14-0abc-4111-8878-e64d749145e2_1709872262.815407.png)
### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/50a9e695-009d-4495-a8dd-df4156b4f62e_1709872337.2743845.png)

## 2. Approach
<!-- Describe your approach to solving the problem. -->
**One-pass** solution (only iterates through the list once).
Explicit explanation has been written along with the code below (see Python3 code).

## 3. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$ worst case
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 4. Code
### 4.1. Python3 (with explanation each line)
```python3 []
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total, max_freq = 0, 0 # Total frequency to return & max_freq to keep track of the current max
        freq_map = defaultdict(int) # Counter dict
        for n in nums:
            freq_map[n] += 1 # Increase the frequency of each number as we see them
            if freq_map[n] > max_freq: # If the frequency of current number is greater than the previous max frequency we've seen before
                total = max_freq = freq_map[n] # That means the current frequency becomes the max frequency, and `total` is also the current max frequency
            elif freq_map[n] == max_freq: # We've added 1 to frequency of current number above but if it's still equal to the previous max frequency 
                total += max_freq # That means there're 2 max frequencies (the previous & current one) so we add them together
        return total
```
### 4.2. C++
```cpp []
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int total = 0, max_freq = 0;
        unordered_map<int,int>freq_map;
        for (int n : nums) {
            freq_map[n]++;
            if (freq_map[n] > max_freq) {
                total = max_freq = freq_map[n];
            }
            else if (freq_map[n] == max_freq) {
                total += max_freq;
            }
        }
        return total;
    }
};
```
### Upvote [here](https://leetcode.com/problems/count-elements-with-maximum-frequency/solutions/4840621/0ms-beats-100-python-c) if you find this solution helpful, thank you 🤍

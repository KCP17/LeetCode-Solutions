# Beats 100%✅🔥🔥🔥| Python, C++💻| SUPER EASY Explanation📕

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/33f8c48e-ea3e-441e-9fae-8ef6fc5df109_1719824836.5668757.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/7a60229d-9b93-4975-87b6-bc5c693d2b36_1719824887.5795708.png)

## 2. Algorithms
* Counting

## 3. Code

### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0 # Keep track of the number of consecutive odds
        for n in arr:
            if n % 2 != 0: # Odd (not divisible by 2) -> Increment `count`
                count += 1
                if count == 3: # Enough of consecutive odds -> True
                    return True
            else: # Even -> Even number breaks the consecutive sequence of odd numbers
                count = 0 # Reset `count`, start counting again as we see an odd number later
        return False # `count` didn't reach 3 at any point of `arr`, must be False
```

### 3.2. C++
```cpp []
class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int count = 0;
        for (int n : arr) {
            if (n % 2 != 0) {
                count++;
                if (count == 3) {
                    return true;
                }
            }
            else {
                count = 0;
            }
        }
        return false;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/three-consecutive-odds/solutions/5395885/beats-100-python-c-super-easy-explanation) if you find this solution helpful, thank you 🤍

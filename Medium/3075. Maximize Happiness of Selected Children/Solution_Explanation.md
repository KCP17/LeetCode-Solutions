# Beats 99.97% Time⌛🔥 99.10% Space💾🔥| Python, C++ 💻 | Clear Explanation📗

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/19967664-6733-4e70-95ce-ecae55ecdcc9_1715251788.976113.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/4e81912b-7388-4f5a-89d1-e643d5e04110_1715251849.2357152.png)

## 2. Algorithms
- Sorting
- Greedy

## 3. Code (with explanation each line)

### 3.1. Python3
```python3 []
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0 # Result
        cur_k = k # Current k after each pick
        happiness.sort() # Top of stack contains max happiness
        
        while cur_k > 0: # While budget is enough for picking (each iteration indicates each pick)
            pick = happiness.pop() # Greedy: always pick top of stack for max happiness
            picked = k - cur_k # Number of times we've picked, and also the amount of happiness to subtract from the current pick
            if pick > picked: # Ensure the current pick will still be positive after subtracting from it
                res += (pick - picked) # Add the positive subtracted happiness to result
            else: # After subtracting, if happiness is still <= 0 even though we tried to be greedy, that means there's nothing more to add to result
                break
            cur_k -= 1 # -1 turn of picking
        
        return res # Result
```

### 3.2. C++
```cpp []
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        long long int res = 0;
        long long int pick = 0, picked = 0;
        int cur_k = k;
        sort(happiness.begin(), happiness.end());

        while (cur_k > 0) {
            pick = happiness.back(); // Greedy: get top of stack
            happiness.pop_back(); // Pop top of stack
            picked = k - cur_k;
            if (pick > picked) {
                res += (pick - picked);
            }
            else {
                break;
            }
            cur_k--;
        }
        return res;
    }
};
```

## 4. Complexity
- Time complexity: $$O(k)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/maximize-happiness-of-selected-children/solutions/5134876/beats-99-97-time-99-10-space-python-c-clear-explanation) if you find this solution helpful, thank you 🤍

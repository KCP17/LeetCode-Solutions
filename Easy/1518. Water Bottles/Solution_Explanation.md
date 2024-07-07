# Beats 100%✅ BOTH Python & C++🔥🔥🔥| SUPER EASY, CLEAR Explanation📗

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/f5230287-1eb4-4b23-9cff-85ce3323f417_1720354868.1938457.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/434c2a18-4602-4a76-8f76-12da99d45f61_1720354907.3373733.png)

## 2. Algorithms
* Math

## 3. Code

### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0 # Result
        full, empty = numBottles, 0 # current number of full and empty bottles
        while full: # Loop until we have no full bottle to drink anymore
            # 1. Drinking phase
            res += full # Drink all current full bottles
            empty += full # Those full bottles we just drank become empty, and we accumulate them to the count of empty bottles
            # 2. Exchanging phase
            exchange = empty / numExchange # Number of full bottles we can get by exchanging the current empty bottles
            full = int(exchange) # Our full bottles after we exchanged
            if exchange == full: # If `empty` is divisible by `numExchange` above, that means we can and we did exchange all our empty bottles
                empty = 0 # Thus there's no empty bottle left
            else: # Else there're some empty bottles left that are not sufficient to exchange 1 full bottle (< numExchange)
                empty -= (numExchange * full) # And those remaining empty bottles are the ones after we subtract the exchanged empty bottles from the initial empty bottles 
        return res # Return result
```

### 3.2. C++
```cpp []
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = 0;
        int full = numBottles, empty = 0;
        float exchange;
        while (full > 0) {
            res += full;
            empty += full;
            exchange = float(empty) / numExchange;
            full = int(exchange);
            if (exchange == full) {
                empty = 0;
            }
            else {
                empty -= (numExchange * full);
            }
        }
        return res;
    }
};
```

## 4. Complexity

- Time complexity: $$O(log(numBottles))$$
- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/water-bottles/solutions/5435179/beats-100-both-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

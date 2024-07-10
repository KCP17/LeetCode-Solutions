# Beats 100%✅🔥🔥🔥| Python, C++💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/2c49589f-64eb-497c-a4ee-5846c7806191_1720642985.0600185.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/a25c3667-0135-4d37-a037-d9c381115daa_1720642952.767589.png)

## 2. Algorithms

* Basic array traversing

## 3. Code

### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0 # Result aka the moves needed to go back to main folder after all operations
        for operation in logs:
            match operation:
                case "../": # If operation is "../" -> go to parent folder -> 1 step closer to main folder
                    res -= 1 if res > 0 else 0 # Thus the needed moves decremented by 1, but only if `res` is a positive number, that means if we're not already at the main folder
                case "./": # Stay in the same folder so nothing changes, just continue
                    continue
                case _: # Any operation other than the two above will go to a child folder -> 1 step further from the main folder
                    res += 1 # Thus the needed moves incremented by 1
        return res # Return result
```

### 3.2. C++
```cpp []
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int res = 0;
        for (string operation : logs) {
            if (operation == "../") {
                res = (res > 0) ? res - 1 : 0;
            }
            else if (operation == "./") {NULL;}
            else {
                res++;
            }
        }
        return res;
    }
};
```

## 4. Complexity

- Time complexity: $$O(n)$$

- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/crawler-log-folder/solutions/5456861/beats-100-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

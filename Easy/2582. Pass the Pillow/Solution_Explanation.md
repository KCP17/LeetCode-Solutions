# CONSTANT Time & Space - Beats 100%✅🔥🔥🔥| Python, C++💻| EASY, CLEAR Explanation📗

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/30292bfd-6362-4ee4-bc9c-a4ebab88efd6_1720272378.9723282.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/149ea010-7c85-4862-b9f2-c3dd63175048_1720272354.8388662.png)

## 2. Algorithms

* Math

## 3. Code

### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time_per_completion = n - 1 # We need `n - 1` seconds to completely pass the pillow through the whole line (from 1 to n or n to 1)
        completed = time // time_per_completion # Count the number of lines we completed the passing of the pillow (we consider both 1 to n and n to 1)
        elapsed = time_per_completion * completed # Seconds elapsed right after we fully passed the pillow the number of `completed` lines
        remaining = time - elapsed # There's only 1 line remaining and because we cannot fully complete this line, we determine the pillow's position by counting the remaining seconds after we've fully completed as many lines as possible
        # As the 1st line goes in "1 to n" direction, if we completed an "even" number of lines, that means the line after those lines should also go in "1 to n" direction, thus the pillow's position is 1 + remaining seconds (since we start at index 1)
        # Else if we completed an "odd" number of lines, the last line should go in "n to 1" direction, that means the pillow's position is the index of person "n" - remaining seconds
        return 1 + remaining if completed % 2 == 0 else n - remaining
```

### 3.2. C++
```cpp []
class Solution {
public:
    int passThePillow(int n, int time) {
        int time_per_completion = n - 1;
        int completed = time / time_per_completion;
        int elapsed = time_per_completion * completed;
        int remaining = time - elapsed;
        return (completed % 2 == 0) ? 1 + remaining : n - remaining;
    }
};
```

## 4. Complexity

- Time complexity: $$O(1)$$

- Space complexity: $$O(1)$$

### Upvote [here](https://leetcode.com/problems/pass-the-pillow/solutions/5428102/constant-time-space-beats-100-python-c-easy-clear-explanation) if you find this solution helpful, thank you 🤍

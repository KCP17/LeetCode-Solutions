# 0ms - Beats 100% 🔥🔥🔥 | Python, C++ 💻 | EASY - CONSTANT Space - Clear explanation 📗
## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. C ++
![image.png](https://assets.leetcode.com/users/images/f57fb3b4-2924-48a5-bbdf-3e5e05b24b17_1712678263.9577212.png)
### 1.2. Python3
![image.png](https://assets.leetcode.com/users/images/4746671e-e24c-4ec5-8052-f6ab7767a85b_1712678275.8687181.png)

## 2. Code (with explanation each line)
### 2.1. Python3
```python3 []
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students) # Number of students prefer to eat square sandwich (sandwich 1)
        zeros = len(students) - ones # Number of students prefer to eat circle sandwich (sandwich 0)
        for s in sandwiches:
            if s == 1: # If sandwich 1 at top of stack
                if ones == 0: # And NO student who prefers sandwich 1 anymore -> NOT a single student can take the sandwich 1 at top of stack
                    return zeros # Then students who prefer sandwich 0 can't have their lunch
                ones -= 1 # If there're still students who prefer sandwich 1 then those students can take the sandwich at top of stack
            else: # If sandwich 0 at top of stack
                if zeros == 0: # And NO one can take sandwich 0 at top of stack -> sandwiches 1 (if exist in stack but not at top) CANNOT be taken also
                    return ones # Then students who prefer sandwich 1 can't have their lunch
                zeros -= 1 # If there're still students who prefer sandwich 0 then those students can take the sandwich at top of stack
        return 0 # No student has to suffer from starving
```
### 2.2. C++
```cpp []
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int ones = accumulate(students.begin(), students.end(), 0);
        int zeros = students.size() - ones;
        for (int s : sandwiches) {
            if (s == 1) {
                if (ones == 0) {
                    return zeros;
                }
                ones--;
            }
            else {
                if (zeros == 0) {
                    return ones;
                }
                zeros--;
            }
        }
        return 0;
    }
};
```
## 3. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/solutions/4999523/0ms-beats-100-python-c-easy-constant-space-clear-explanation) if you find this solution helpful, thank you 🤍

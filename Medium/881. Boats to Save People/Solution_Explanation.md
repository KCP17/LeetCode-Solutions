# Beats 98.94%✅| Explicit VIDEO Explanation + Visualization + Simulation📙| Python, C++ 💻

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/c18fd50d-119c-4468-99b8-8cbcf810eb8c_1715005453.0016093.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/270f23e7-a9e5-41a4-9a44-e8c34bb9cc89_1715005655.784192.png)

## 2. Algorithms
- Sorting
- Two Pointers
- Greedy
## 3. Explanation
_Click on this image to watch my YouTube explanation video_
[![Click on this image to watch the YouTube explanation video](https://i.ytimg.com/vi/KRHzbHnw1rE/maxresdefault.jpg)](https://youtu.be/KRHzbHnw1rE?si=XeZ0FYCo8mDVJo92)

## 4. Code
### 4.1. Python3
```python3 []
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0 # Boats needed to use
        people.sort() # Ascending
        l, r = 0, len(people) - 1 # Left & Right pointers
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1 # Try to carry "left" if possible
            r -= 1 # Always carry "right"
            res += 1 # +1 boat used
        return res
```
### 4.2. C++
```cpp []
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int res = 0;
        sort(people.begin(), people.end());
        int l = 0, r = people.size() - 1;
        while (l <= r) {
            if (people[l] + people[r] <= limit) {
                l++;
            }
            r--;
            res++;
        }
        return res;
    }
};
```
## 5. Complexity (Explained in the video)
- Time complexity:
  - Average: $$O(N*log(N) + N/2)$$
  - Worst case: $$O(N*log(N) + N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/boats-to-save-people/solutions/5121100/beats-9894-explicit-video-explanation-visualization-simulation-python-c) if you find this solution helpful, thank you 🤍

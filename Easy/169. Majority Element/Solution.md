## Efficiency
### Python3
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e6d37092-2e32-4cec-af39-5173a5ac5aff)
### C++
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/876dc554-dc8c-4322-90a5-7030ebbd1783)

## Code
### Python3
```python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        avg = len(nums) // 2
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > avg:
                return n
```
### C++
```cpp []
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int avg = nums.size() / 2;
        unordered_map<int,int>count;
        for (int n: nums) {
            count[n]++;
            if (count[n] > avg) {
                return n;
            }
        }
        return 0;
    }
};
```
## Time & Space:
* Time: $$O(N)$$
* Space: $$O(N)$$ doesn't satisfy follow-up requirements

# Beats 93.23%✅🔥| Python, C++💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof

### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/9a0aa5bb-ff3e-4f90-af74-0aacb8b04a01_1722646928.0482569.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/8d47034a-fd1b-431b-8427-d56f9ebc3838_1722647132.8464537.png)

## 2. Algorithms
* Hash Map
* Counting

## 3. Code
### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash_target = defaultdict(int) # Counting HashMap for `target`
        hash_arr = defaultdict(int) # Counting HashMap for `arr`
        N = len(target)
        for i in range(N):
            hash_target[target[i]] += 1 # Hash each element of `target` and count its frequency
            hash_arr[arr[i]] += 1 # Hash each element of `arr` and count its frequency
        return hash_target == hash_arr # If elements of 2 arrays are the same and have same frequencies, then they can be equal
```
### 3.2. C++
```cpp []
class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        unordered_map<int,int>hash_target;
        unordered_map<int,int>hash_arr;
        int N = target.size();
        for (int i=0; i < N; i++) {
            hash_target[target[i]]++;
            hash_arr[arr[i]]++;
        }
        return hash_target == hash_arr;
    }
};
```

## 4. Complexity
- Time complexity: $$O(N)$$
- Space complexity: $$O(2N)$$

### Upvote [here](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/solutions/5576817/beats-93-23-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

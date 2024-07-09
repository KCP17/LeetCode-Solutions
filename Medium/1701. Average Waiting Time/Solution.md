## 1. Efficiency
## 1.1. Python3
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/1f321fca-6e87-470a-9eaa-67ddf5c99586)
## 1.2. C++
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/9ee01386-bfa6-4a98-b7c9-00b3aa6bd8af)

## 2. Code
### 2.1. Python3
```python3 []
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        idle_time = 1
        for original_arrival, cooking_time in customers:
            total_time += cooking_time
            pending_time = idle_time - original_arrival
            if pending_time > 0:
                total_time += pending_time
                idle_time += cooking_time
            else:
                idle_time = original_arrival + cooking_time
        return total_time / len(customers)
```
### 2.2. C++
```cpp []
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double total_time = 0;
        int idle_time = 1, pending_time, original_arrival, cooking_time;
        for (int i=0; i < customers.size(); i++) {
            original_arrival = customers[i][0];
            cooking_time = customers[i][1];
            total_time += cooking_time;
            pending_time = idle_time - original_arrival;
            if (pending_time > 0) {
                total_time += pending_time;
                idle_time += cooking_time;
            }
            else {
                idle_time = original_arrival + cooking_time;
            }
        }
        return total_time / customers.size();
    }
};
```

## 3. Note:
My solution:
- Time: $$O(n)$$
- Space: $$O(1)$$
[ Time taken: 18 m 2 s ]

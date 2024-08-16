## 1. Efficiency
### 1.1. Python3
![image](https://github.com/user-attachments/assets/1f683e92-a833-43f4-9a1a-74a2d1608a19)

### 1.2. C++
![image](https://github.com/user-attachments/assets/d7df4baa-33bd-440c-9886-ede3b139ed84)

## 2. Code
### 2.1. Python3
```python3 []
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for b in bills:
            change[b] += 1
            match b:
                case 10:
                    if change[5] > 0:
                        change[5] -= 1
                    else:
                        return False
                case 20:
                    if change[5] > 0 and change[10] > 0:
                        change[10] -= 1
                        change[5] -= 1
                    elif change[5] > 2:
                        change[5] -= 3
                    else:
                        return False
        return True
```
### 2.2. C++
```cpp []
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        unordered_map<int, int>change;
        for (int b : bills) {
            change[b]++;
            switch (b) {
                case 10:
                    if (change[5] > 0) {
                        change[5]--;
                    }
                    else {
                        return false;
                    }
                    break;
                case 20:
                    if ((change[5] > 0) && (change[10] > 0)) {
                        change[10]--;
                        change[5]--;
                    }
                    else if (change[5] > 2) {
                        change[5] -= 3;
                    }
                    else {
                        return false;
                    }
                    break;
            }
        }
        return true;
    }
};
```

## 3. Note:
HashMap (My solution):
- Time: $$O(n)$$
- Space: $$O(3)$$

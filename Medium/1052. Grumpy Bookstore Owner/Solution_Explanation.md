# Beats 94.79%✅| Python 💻 | CONCISE Explanation📙

## 1. Proof (Python3)
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/2a94ea40-f9b8-4204-b4bb-60502688b6f3_1718980144.0168397.png)

## 2. Algorithms
* Sliding Window

## 3. Code - Python3 (with concise explanation)
```python3 []
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 1. Set up consecutive range `minutes` that the bookstore owner's technique can be used, sum up the satisfied customers without the technique simultaneously
        sat_cust_NO_tech = 0
        cur_sat_cust_YES_tech = 0
        for i in range(minutes):
            if grumpy[i]:
                cur_sat_cust_YES_tech += customers[i]
            else:
                sat_cust_NO_tech += customers[i]
        max_sat_cust_YES_tech = cur_sat_cust_YES_tech
        
        # 2. Keep track of the `max_sat_cust_YES_tech` aka the max satisfied customers this technique can bring, also continue to sum up the satisfied customers without the technique
        left, right = 0, minutes - 1
        N = len(customers) - 1
        while right < N:
            # Move left pointer
            cur_sat_cust_YES_tech -= (customers[left] * grumpy[left])
            left += 1
            # Move right pointer
            right += 1
            cur_sat_cust_YES_tech += (customers[right] * grumpy[right])
            # Update max
            max_sat_cust_YES_tech = max(max_sat_cust_YES_tech, cur_sat_cust_YES_tech)
            # Increment satisfied customers without the technique
            sat_cust_NO_tech += customers[right] if not grumpy[right] else 0

        return sat_cust_NO_tech + max_sat_cust_YES_tech
```

## 4. Complexity
![image.png](https://assets.leetcode.com/users/images/7c64347d-27d1-429d-af4b-b659b9ef7d12_1718980273.406037.png)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

![image.png](https://assets.leetcode.com/users/images/5a6bf494-cff6-4202-beaf-a55318e6172e_1718980311.7271442.png)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/grumpy-bookstore-owner/solutions/5347457/beats-94-79-python-concise-explanation) if you find this solution helpful, thank you 🤍

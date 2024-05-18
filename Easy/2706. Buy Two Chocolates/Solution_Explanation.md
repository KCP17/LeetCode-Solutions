# Python EASIEST solution - Beats 99.38% ✅🔥

## 1. Proof
![leetcode_solution_buychoco.png](https://assets.leetcode.com/users/images/4df90dc2-4d18-447d-b90b-08f24ef51b8b_1703094264.7908518.png)

## 2. Intuition
Basically just searching for the two smallest values in the prices.

## 3. Approach
Find the smallest value in the original 'prices' list -> choco1_min
Then remove that value in the list
Find the smallest value in the modified list -> choco2_min
After finding those values, the remaining job is a piece of cake

## 4. Complexity
- Time complexity: $O(n) - linear$ 

- Space complexity: $O(1) - constant$

## 5. Code (Python)
```python []
class Solution():
    def buyChoco(self, prices, money):
        
        choco1_min = prices[0]
        for price in prices[1:]:
            if price < choco1_min:
                choco1_min = price

        prices.remove(choco1_min)
        
        choco2_min = prices[0]
        for price in prices[1:]:
            if price < choco2_min:
                choco2_min = price
        
        leftover = money - (choco1_min + choco2_min)
        return leftover if leftover >= 0 else money
```
### Upvote [here](https://leetcode.com/problems/buy-two-chocolates/solutions/4431740/python-easiest-solution-beats-99-38) if you find this solution helpful, thank you 🤍

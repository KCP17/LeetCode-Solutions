# Beats 96.10%✅🔥| Python💻| SUPER EASY, CLEAR Explanation📕

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/7b8d791b-3d14-46fb-9637-db9c0bdaaa5a_1721665366.979954.png)

## 2. Algorithms
* Zipping
* Sorting

## 3. Code - Python3 (with inline explanation)
```python3 []
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip heights and names to tuples where each tuple is (heights[i], names[i])
        # Then sort based on the heights, and with reverse (descending)
        sorted_heights = sorted(zip(heights, names), reverse=True)
        # Append the names in the sorted order (2nd element of each tuple)
        res = [n for h, n in sorted_heights]
        return res
```

## 4. Complexity

- Time complexity: $$O(N*log(N) + N)$$

- Space complexity: $$O(N)$$

### Upvote [here](https://leetcode.com/problems/sort-the-people/solutions/5518092/beats-96-10-python-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

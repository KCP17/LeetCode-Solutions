# 🐍 Python BUILD FROM SCRATCH Solution 📝 | For Learning 📐
## 1. Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Since the vertical lines are infinite, we don't need to care about the y coordinates of the points, and only focus on the x coordinates.
- The `x_cors` indicate the positions of the lines.
- Therefore, finding the max width, or longest distance between 2 consecutive lines is the same as finding the max distance between 2 points horizontally.

## 2. Illustration
![Widest vertical area between 2 pts contain no pts.jpg](https://assets.leetcode.com/users/images/2cc39a0d-da62-42f8-8e1c-72590e613e26_1703143588.4311333.jpeg)

## 3. Approach
<!-- Describe your approach to solving the problem. -->
1. Use quicksort to sort the x coordinates of the points in ascending order.
2. Iterate through the sorted list & calculate the distance between adjacent sorted points by subtracting the `x_cor` of this from another.
3. At the same time, find the max `x_cor` of calculated distances.
4. The max `x_cor` is the max width we're looking for.

***!!! This approach is not time efficient, but great for learning and understanding the underlying principles of algorithms (quicksort & maximum search).***

## 4. Complexity
- Time complexity: $O(n*log(n))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## 5. Code (Python)
```python []
class Solution():
    def maxWidthOfVerticalArea(self, points):
        x_cors = []
        for point in points:
            x_cors.append(point[0])

        sorted_x_cors = self.quicksort(x_cors)

        max_width = 0
        for i in range(len(sorted_x_cors)-1):
            distance = sorted_x_cors[i+1] - sorted_x_cors[i]
            if distance > max_width:
                max_width = distance

        return max_width
    
    def quicksort(self, x_cors):
        if len(x_cors) <= 1: return x_cors
        pivot = x_cors[0]
        less_than_pivot = []
        greater_than_pivot = []

        for x_cor in x_cors[1:]:
            if x_cor < pivot:
                less_than_pivot.append(x_cor)
            else:
                greater_than_pivot.append(x_cor)
        
        return self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot)
```
### Upvote [here](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/solutions/4434402/python-build-from-scratch-solution-for-learning) if you find this solution helpful, thank you 🤍

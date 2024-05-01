# Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/b7cf0833-57f9-47cb-8fe9-125dc0da3c09_1704210921.1447852.png)


# Approach
<!-- Describe your approach to solving the problem. -->
***Using Hash Table**
1. Create a hashMap, a 2D array with an initial sub-array, a variable to indicate the number of sub-lists.
2. Loop through each element of the original array.
3. If the current number is not seen before, add it to the hashMap along with the its seen times (the number of times that number is seen before, in this case it's 0 since we haven't seen this number before).
4.  If the number is seen already, add 1 to the seen times to indicate we saw it one more time. Also, check if the seen times of this number exceeded the number of sub-lists or not, if it is then we add another sub-list, and reassign the number of sub-lists.
5. Subsequently, add the number to the correct sub-list (indicated by the number of seen times). By this way, a number will never be added to the sub-list which contained it already, because we added 1 to the index if the number's been seen (step 4) before we do this appending thing.
6. Finally, return the 2D result.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code (Python3)
```python3 []
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        result = [[]]
        curr_max = 0

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            else:
                hashMap[num] += 1
                if hashMap[num] > curr_max:
                    result.append([])
                    curr_max = hashMap[num]

            result[hashMap[num]].append(num)

        return result
```
![upvote img.png](https://assets.leetcode.com/users/images/b40339b2-8e83-4749-8b5d-c34b9172ea90_1704213128.8545456.png)

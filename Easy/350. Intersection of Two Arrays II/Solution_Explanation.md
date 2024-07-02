# Beats 95.24%✅| Python💻| EASY, CLEAR Explanation📗

## 1. Proof (Python3)
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/d953fbc0-e95d-438b-a48e-189164e4849b_1719935087.2588286.png)

## 2. Algorithms
* Hash Map
* Counting

## 3. Code - Python3 (with explanation)
```python3 []
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cnt_1 = Counter(nums1) # Maps each number to its frequency
        cnt_2 = Counter(nums2) # Same with the one above
        for n in cnt_1.keys(): # Get all numbers in `nums1`
            if n in cnt_2: # If that also exists in `nums2` (Exists in both arrays)
                freq = min(cnt_1[n], cnt_2[n]) # We only go for the smaller frequency between 2 arrays because using the higher results in insufficient frequency of the other array
                for _ in range(freq):
                    res.append(n) # Append "lower frequency" times of `n`
        return res # Return result
```

## 4. Complexity
- Time complexity: $$O(2n +m)$$ with `n=len(nums1)`, `m=len(nums2)`
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n+m)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/intersection-of-two-arrays-ii/solutions/5404208/beats-95-24-python-easy-clear-explanation) if you find this solution helpful, thank you 🤍

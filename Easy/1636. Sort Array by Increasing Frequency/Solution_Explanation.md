# Beats 98.62%✅🔥| Python💻| CLEAR, CONCISE Explanation📗

## 1. Proof (Python3)
![image.png](https://assets.leetcode.com/users/images/d133fe70-782d-4558-9aad-7b8dcbd43c5d_1721749510.5258894.png)

## 2. Algorithms
* Hash Map
* Counting
* Sorting

## 3. Code - Python3 (with inline explanation)
```python3 []
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of every number
        count = Counter(nums)
        # Maps each frequency to a list of numbers of that frequency
        freq_map = defaultdict(list)
        for n, occ in count.items():
            freq_map[occ].append(n)
        # Sort the frequency values in ascending order
        sorted_map = sorted(list(freq_map.items()))
        # Adding the numbers to our result list
        res = []
        for freq, numbers in sorted_map:
            for each in sorted(numbers, reverse=True): # Sort the same-frequency numbers in descending order, and iterate through each of those sorted numbers
                for _ in range(freq):
                    res.append(each) # Append a number "its frequency" times
        return res
```

## 4. Complexity
Let `N` be the size of the input array, `M` be the amount of different frequencies of all numbers.
- Time complexity: $$O(N + M + Nlog(N) + Mlog(M))$$
- Space complexity: $$O(N + M)$$

### Upvote [here](https://leetcode.com/problems/sort-array-by-increasing-frequency/solutions/5523502/beats-98-62-python-clear-concise-explanation) if you find this solution helpful, thank you 🤍

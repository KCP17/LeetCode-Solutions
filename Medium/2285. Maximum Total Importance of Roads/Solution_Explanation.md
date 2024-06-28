# Beats 94.48%✅| Python, C++💻| SUPER EASY, CLEAR Explanation📙

## 1. Proof
<!-- Describe your first thoughts on how to solve this problem. -->
### 1.1. Python3
![image.png](https://assets.leetcode.com/users/images/20fcd273-1a64-49f0-bf4d-60b5e6c01768_1719573117.9644432.png)

### 1.2. C++
![image.png](https://assets.leetcode.com/users/images/4378986f-1bb8-4c6b-83b6-814a4090cbaa_1719573153.367877.png)

## 2. Algorithms
* Greedy
* Sorting

## 3. Code

### 3.1. Python3 (with inline explanation)
```python3 []
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        '''
        We simply want to be greedy and assign the greatest value to the city which involves in most roads, the 2nd greatest value to the 2nd most-involved city, and so on...
        In that way, we can use our greatest value the most times in our sum, likewise the 2nd greatest value the 2nd most times, and so on ==> We maximize our result eventually
        '''
        # 1. Count the appearances (involvement) of each city and sort those appearances in descending order (from greatest to smallest)
        links = [0 for _ in range(n)] # i: the city, links[i]: the number of cities that city `i` links to aka the number of roads that city `i` involves in
        for ct1, ct2 in roads: # For each road we see, we increment the appearances (involvement) of both city 1 & city 2 of that road
            links[ct1] += 1 # Increment involvement of city 1
            links[ct2] += 1 # Increment involvement of city 2
        links.sort(reverse=True) # Sort in descending order so the city with most appearances is at index 0, and number of appearances decreases as we go to the right
        
        # 2. We go from the most-appearance city & assign the greatest value `n` to it, then the 2nd most with the 2nd greatest value `n - 1`, and so on for the remaining cities
        res = 0 # Result
        for ct_appearances in links: # With each city
            res += (ct_appearances * n) # We add its assigned value `n` times to our result 
            n -= 1 # Then we decrement the value `n` so this will be the assigned value for the next city
        
        return res
```

### 3.2. C++
```cpp []
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        cout << n;
        vector<long long>links(n, 0);
        for (auto& cities : roads) {
            links[cities[0]]++;
            links[cities[1]]++;
        }
        sort(links.begin(), links.end(), greater<long long>());

        long long res = 0;
        for (long long ct_appearances : links) {
            res += (ct_appearances * n);
            n--;
        }

        return res;
    }
};
```

## 4. Complexity
- Time complexity: $$O(M + 2N + N*log(N))$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
** N = number of cities, M = number of roads

### Upvote [here](https://leetcode.com/problems/maximum-total-importance-of-roads/solutions/5382560/beats-94-48-python-c-super-easy-clear-explanation) if you find this solution helpful, thank you 🤍

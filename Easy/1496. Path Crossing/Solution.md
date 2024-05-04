## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/445362ff-0232-414c-9ce0-3a0d3fb07647)

## Code (Python)
```python []
class Solution:
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        hashMap = set()
        x = y = 0
        hashMap.add((0,0))
        
        for direction in path:
            
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            coordinate = (x,y)

            if coordinate in hashMap:
                return True
            
            hashMap.add(coordinate)

        return False
```
## Note:
HashMap - 0ms, beats 100% (My solution):
- Time: $$O(N)$$
- Space: $$O(N)$$

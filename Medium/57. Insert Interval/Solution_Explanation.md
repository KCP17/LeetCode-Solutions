## 1. Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/0fef056b-e842-4a33-8561-0daf2101a9af)

## 2. Code (Python3) with explanation each line
```python3 []
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval] # Edge case

        for i in range(len(intervals)): # Insert `newInterval` into correct position to maintain sorted ascending order
            if intervals[i][0] > newInterval[0]: # Whenever it sees a start time in `intervals` that is later than the start time of `newInterval`
                intervals.insert(i, newInterval) # Insert the `newInterval` and push all other remaining intervals to the right
                break
            elif i == len(intervals) - 1: # If it comes to the last index but not inserted yet means start time of `newInterval` is the latest so just append it
                intervals.append(newInterval)

        new_intervals = [intervals[0]] # Stack (our result) with default first element
        for cur in intervals[1:]: # Loop through remaining elements of original `intervals` to merge & add intervals to `new_intervals` (our result)
            if new_intervals[-1][0] <= cur[0] <= new_intervals[-1][1]: # If start time of `cur` is in between start time & end time of top of stack (Overlapped)
                new_intervals[-1][1] = max(new_intervals[-1][1], cur[1]) # Adjust end time of top of stack to be the latest between itself and end time of `cur` (Merge)
            else: # If start time of `cur` > end time of top of stack (cuz cur's start time is not in the range above and it's not earlier than start time of top of stack cuz we've sorted before)
                new_intervals.append(cur) # Push to stack the cur interval

        return new_intervals # The stack is our result
```
## 3. Note:
Stack (My solution):
- Time: $$O(2N)$$
- Space: $$O(1)$$ as returned array is not counted towards memory

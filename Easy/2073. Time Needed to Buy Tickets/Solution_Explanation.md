## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/38f1fb3f-b724-49e4-947e-2aa43907778b)

## Code (Python3) - with explanation each line
```python3 []
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        tickets[k] = -tickets[k] # Mark the `k` position as negative
        queue = deque(tickets) # Create a queue
        
        while True: # Each iteration is each time a person buys ticket
            res += 1 # A person buys ticket so time += 1
            person_tickets = queue.popleft() # Person stands out and gets ready to buy ticket
            
            if person_tickets > 1: # For other people that are not the `k` one cuz it has negative value (if > 1 means need to buy more so go to the back)
                queue.append(person_tickets - 1) # Buys the ticket then go to the back
            
            elif person_tickets < 0: # Negative value -> only for the `k` person
                if person_tickets == -1: # If only 1 ticket left but since we've already counted this ticket (res += 1 in this iteration)
                    return res # So return res
                queue.append(person_tickets + 1) # Else buys the ticket then go to the back
```
## Note:
Queue (My solution):
- Time: $$O(S * log(S))$$ with S = sum(tickets)
- Space: $$O(N)$$

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        idle_time = 1
        for original_arrival, cooking_time in customers:
            total_time += cooking_time
            pending_time = idle_time - original_arrival
            if pending_time > 0:
                total_time += pending_time
                idle_time += cooking_time
            else:
                idle_time = original_arrival + cooking_time
        return total_time / len(customers)

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 1. Set up consecutive range `minutes` that the bookstore owner's technique can be used, sum up the satisfied customers without the technique simultaneously
        sat_cust_NO_tech = 0
        cur_sat_cust_YES_tech = 0
        for i in range(minutes):
            if grumpy[i]:
                cur_sat_cust_YES_tech += customers[i]
            else:
                sat_cust_NO_tech += customers[i]
        max_sat_cust_YES_tech = cur_sat_cust_YES_tech
        
        # 2. Keep track of the `max_sat_cust_YES_tech` aka the max satisfied customers this technique can bring, also continue to sum up the satisfied customers without the technique
        left, right = 0, minutes - 1
        N = len(customers) - 1
        while right < N:
            # Move left pointer
            cur_sat_cust_YES_tech -= (customers[left] * grumpy[left])
            left += 1
            # Move right pointer
            right += 1
            cur_sat_cust_YES_tech += (customers[right] * grumpy[right])
            # Update max
            max_sat_cust_YES_tech = max(max_sat_cust_YES_tech, cur_sat_cust_YES_tech)
            # Increment satisfied customers without the technique
            sat_cust_NO_tech += customers[right] if not grumpy[right] else 0

        return sat_cust_NO_tech + max_sat_cust_YES_tech

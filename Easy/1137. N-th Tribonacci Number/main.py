class Solution:
    def tribonacci(self, n: int) -> int:
        match n: # Edge cases
            case 0: return 0
            case 1 | 2: return 1 # case 1 or 2
        
        T_first, T_mid, T_last = 0, 1, 1
        for i in range(n - 2):
            T_next = T_first + T_mid + T_last
            T_first, T_mid, T_last = T_mid, T_last, T_next # [0 (first), 1 (mid), 2 (last)] 3 (next) -> 0 [1 (first), 2 (mid), 3 (last)]
        return T_next

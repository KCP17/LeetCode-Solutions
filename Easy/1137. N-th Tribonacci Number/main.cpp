class Solution {
public:
    int tribonacci(int n) {
        switch (n) {
            case 0:
                return 0;
            case 1:
            case 2:
                return 1;
        }
        int T_first = 0, T_mid = 1, T_last = 1;
        int T_next;
        for (int i=0; i < n-2; i++) {
            T_next = T_first + T_mid + T_last;
            T_first = T_mid, T_mid = T_last, T_last = T_next;
        }
        return T_next;
    }
};

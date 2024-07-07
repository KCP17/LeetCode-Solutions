class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = 0;
        int full = numBottles, empty = 0;
        float exchange;
        while (full > 0) {
            res += full;
            empty += full;
            exchange = float(empty) / numExchange;
            full = int(exchange);
            if (exchange == full) {
                empty = 0;
            }
            else {
                empty -= (numExchange * full);
            }
        }
        return res;
    }
};

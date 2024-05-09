class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        long long int res = 0;
        long long int pick = 0, picked = 0;
        int cur_k = k;
        sort(happiness.begin(), happiness.end());

        while (cur_k > 0) {
            pick = happiness.back(); // Greedy: get top of stack
            happiness.pop_back(); // Pop top of stack
            picked = k - cur_k;
            if (pick > picked) {
                res += (pick - picked);
            }
            else {
                break;
            }
            cur_k--;
        }
        return res;
    }
};

class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int res = 0;
        vector<int>odds;
        int amount = 0, removed = -1, oldest = 0;
        int N = nums.size();
        for (int i=0; i<N; i++) {
            if (nums[i] % 2 != 0) {
                odds.push_back(i);
                amount++;
            }
            if (amount > k) {
                removed = odds[oldest];
                oldest++;
                amount--;
            }
            if (amount == k) {
                res += (odds[oldest] - removed);
            }
        }
        return res;
    }
};

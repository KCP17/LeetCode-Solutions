class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        // 1. Counting (bucket) sort
        int max_index = *max_element(nums.begin(), nums.end()) + 1;
        vector<int> nums_cnt(max_index, 0);
        for (int n : nums) {
            nums_cnt[n]++;
        }

        // 2. Count the moves
        int res = 0;
        int carry = 0;
        for (int occ : nums_cnt) {
            res += carry;
            if (occ == 0) {
                if (carry > 0) {
                    carry--;
                }
            }
            else {
                carry += (occ - 1);
            }
        }
        
        // 3. Add remaining moves
        if (carry > 0) {
            res += ((1 + carry) * (carry / 2.0));
        }

        // 4. Return result
        return int(res);
    }
};

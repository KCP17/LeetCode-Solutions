class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;

        while ((nums[l] < 0) && (nums[r] > 0)) {
            int neg = abs(nums[l]), pos = nums[r];
            if (neg == pos) {
                return pos;
            }
            else if (neg < pos) {
                r--;
            }
            else {
                l++;
            }
        }
        return -1;
    }
};

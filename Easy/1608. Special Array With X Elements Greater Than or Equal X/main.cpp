class Solution {
public:
    int specialArray(vector<int>& nums) {
        int N = nums.size();
        sort(nums.begin(), nums.end());
        int x, max_of_left;
        for (int i=0; i < N; i++) {
            x = N - i;
            max_of_left = (i - 1 >= 0) ? nums[i - 1] : 0;
            if ((nums[i] >= x) && (x > max_of_left)) {
                return x;
            }
        }
        return -1;
    }
};

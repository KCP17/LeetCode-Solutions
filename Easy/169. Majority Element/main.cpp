class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int avg = nums.size() / 2;
        unordered_map<int,int>count;
        for (int n: nums) {
            count[n]++;
            if (count[n] > avg) {
                return n;
            }
        }
        return 0;
    }
};

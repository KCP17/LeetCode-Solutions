class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int total = 0, max_freq = 0;
        unordered_map<int,int>freq_map;
        for (int n : nums) {
            freq_map[n]++;
            if (freq_map[n] > max_freq) {
                total = max_freq = freq_map[n];
            }
            else if (freq_map[n] == max_freq) {
                total += max_freq;
            }
        }
        return total;
    }
};

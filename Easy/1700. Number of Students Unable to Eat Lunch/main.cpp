class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int ones = accumulate(students.begin(), students.end(), 0);
        int zeros = students.size() - ones;
        for (int s : sandwiches) {
            if (s == 1) {
                if (ones == 0) {
                    return zeros;
                }
                ones--;
            }
            else {
                if (zeros == 0) {
                    return ones;
                }
                zeros--;
            }
        }
        return 0;
    }
};

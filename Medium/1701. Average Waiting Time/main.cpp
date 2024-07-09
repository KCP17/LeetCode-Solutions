class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double total_time = 0;
        int idle_time = 1, pending_time, original_arrival, cooking_time;
        for (int i=0; i < customers.size(); i++) {
            original_arrival = customers[i][0];
            cooking_time = customers[i][1];
            total_time += cooking_time;
            pending_time = idle_time - original_arrival;
            if (pending_time > 0) {
                total_time += pending_time;
                idle_time += cooking_time;
            }
            else {
                idle_time = original_arrival + cooking_time;
            }
        }
        return total_time / customers.size();
    }
};

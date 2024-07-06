class Solution {
public:
    int passThePillow(int n, int time) {
        int time_per_completion = n - 1;
        int completed = time / time_per_completion;
        int elapsed = time_per_completion * completed;
        int remaining = time - elapsed;
        return (completed % 2 == 0) ? 1 + remaining : n - remaining;
    }
};

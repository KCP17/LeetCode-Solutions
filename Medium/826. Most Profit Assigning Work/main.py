class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        '''
        1. Prepare our "greedy" materials
        '''
        pro_diff = sorted(zip(profit, difficulty), reverse=True) # Sort the profit by descending order (each tuple contains each profit[i] links with its corresponding difficulty[i])
        worker.sort() # Ascending order
        cur_wk = len(worker) - 1 # Pointer starts from the last index of `worker` - the worker with highest ability (because we sorted)
        res = 0 # Result
        '''
        2. Greedy
            - Going from the job with most profit and sequentially to least profit (sorted)
            - At each job, count the number of valid workers with each worker satisfies the condition worker's ability > job's difficulty
            - We calculate the profit that those valid workers can generate by doing this job = number of valid workers for this job * this job's profit
            - As we go from the highest-profit job and count all the eligible workers, we get the max profit for this job, the same logic applies with lower-profit jobs
            => We get the max profit of each job, add them together, thus we have the max profit of all
            * If the condition worker's ability > job's diff is wrong, and we know the remaining workers all have lower abilities (sorted) -> we had max number of valid workers
            ** Workers that the pointer went past are the ones that have been assigned jobs, others are remaining workers with availability of receiving jobs
        '''
        for cur_pro, cur_diff in pro_diff: # For profit and difficulty of each job
            valid_workers = 0 # We initially have 0 valid workers for this job and 
            while cur_wk >= 0 and worker[cur_wk] >= cur_diff: # If there're still worker(s) and worker's ability > job's difficulty
                valid_workers += 1 # This `cur_wk` can do this `cur_diff` job
                cur_wk -= 1 # Move on to next lower-ability worker
            res += (cur_pro * valid_workers) # Adding the profit these valid workers can generate by doing this job
        return res # Final result

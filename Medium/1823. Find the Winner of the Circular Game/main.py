class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([n for n in range(1, n + 1)])
        while len(q) > 1:
            for count in range(1, k + 1):
                n = q.popleft()
                if count != k:
                    q.append(n)
        return q[-1]

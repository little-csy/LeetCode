import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        n = len(jobs)
        dp = [0] * (n+1)

        ends = [job[1] for job in jobs]

        for i in range(1,n+1):
            s, e, p = jobs[i-1]

            j = bisect.bisect_right(ends, s) -1

            if j>=0:
                take = p + dp[j+1]
            else:
                take = p
            
            not_take = dp[i-1]
            dp[i] = max(not_take, take)

        return dp[n]
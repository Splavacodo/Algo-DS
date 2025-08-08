class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s) + 1
        m = len(t) + 1

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[-1][-1]
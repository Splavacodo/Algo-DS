class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s) + 1
        m = len(p) + 1

        dp = [[False for _ in range(m)] for _ in range(n)]

        dp[0][0] = True
        
        for j in range(1, m):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, n):
            for j in range(1, m):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]

                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[-1][-1]
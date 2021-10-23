def minimumNumberOfDeletions(S):
    s1 = S
    s2 = S[::-1]
    m = len(s1)
    dp = [[None for _ in range(m+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return m - dp[m][m]
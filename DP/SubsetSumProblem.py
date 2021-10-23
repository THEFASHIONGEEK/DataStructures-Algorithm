def isSubsetSum (N, arr, sum):
    dp = [[False for _ in range(sum+1)] for _ in range(N+1)]   
    for i in range(N+1):
        for j in range(sum+1):
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return 1 if dp[N][sum] else 0
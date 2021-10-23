def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    arr_sum = sum(nums)
    if arr_sum % 2 == 1:
        return False
    else:
        half_sum = arr_sum // 2
        dp = [[False for _ in range(half_sum+1)] for _ in range(n+1)]  
        for i in range(n+1):
            for j in range(half_sum+1):
                if j == 0:
                    dp[i][j] = True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][half_sum]
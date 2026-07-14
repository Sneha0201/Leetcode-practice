# Climbing Stairs
n = 4
def ClimbingStairs(n):
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(ClimbingStairs(n))
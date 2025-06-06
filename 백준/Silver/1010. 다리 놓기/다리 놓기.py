t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = j    
            else: 
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                
    print(dp[n][m])